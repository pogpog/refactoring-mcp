import argparse
import hashlib
import json
import os
import pickle
import re
import sys
from pathlib import Path

import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"


def _default_index_dir() -> Path:
    cache_root = os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache"
    return Path(cache_root) / "refactoring-python-mcp"


# The knowledge base ships inside the package; override to index any folder of
# markdown files (e.g. an Obsidian vault).
VAULT_DIR = Path(
    os.environ.get("REFACTORING_PYTHON_MCP_VAULT_DIR") or Path(__file__).parent / "md_files"
).expanduser().resolve()

# The index must NOT live next to __file__: under uvx/pipx that is an ephemeral
# site-packages that can be rebuilt at any time.
INDEX_DIR = Path(
    os.environ.get("REFACTORING_PYTHON_MCP_INDEX_DIR") or _default_index_dir()
).expanduser()

MANIFEST_FILE = "manifest.json"

_model = None
_index_cache = None


def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    try:
        end = text.index("\n---\n", 4)
    except ValueError:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5:].lstrip("\n")
    meta = {}
    for line in fm_text.splitlines():
        if ": " in line:
            k, _, v = line.partition(": ")
            meta[k.strip()] = v.strip()
    if "tags" in meta:
        tags_raw = meta["tags"].strip("[]")
        meta["tags"] = [t.strip() for t in tags_raw.split(",") if t.strip()]
    return meta, body


def _make_chunk(file_path, page_title, section, tags, content) -> dict:
    return {"file_path": file_path, "page_title": page_title, "section": section, "tags": tags, "content": content}


def _chunk_document(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    meta, body = _parse_frontmatter(text)
    tags = meta.get("tags", [])
    relative = str(path.relative_to(VAULT_DIR))

    title_match = re.search(r"^# (.+)$", body, re.MULTILINE)
    page_title = title_match.group(1).strip() if title_match else path.stem

    parts = re.split(r"(?m)^(## .+)$", body)
    chunks = []

    intro = parts[0].strip()
    if intro:
        chunks.append(_make_chunk(relative, page_title, "", tags, f"{page_title}\n\n{intro}"))

    for i in range(1, len(parts), 2):
        heading = parts[i].lstrip("#").strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        if content:
            chunks.append(_make_chunk(
                relative, page_title, heading, tags,
                f"{page_title} — {heading}\n\n{content}"
            ))

    return chunks


def _vault_fingerprint() -> dict:
    """Identify the vault contents so a stale index is detected and rebuilt.

    Covers the embedding model and every file's relative path and content — so
    a new package version with changed pages, or a different
    REFACTORING_PYTHON_MCP_VAULT_DIR, never silently reuses an old index. Content is
    hashed (not mtimes or the vault's absolute path) because uvx/pipx may
    re-extract the package into a new location on reinstall.
    """
    h = hashlib.sha256()
    for md_file in sorted(VAULT_DIR.rglob("*.md")):
        h.update(str(md_file.relative_to(VAULT_DIR)).encode() + b"\0")
        h.update(hashlib.sha256(md_file.read_bytes()).digest())
    return {"model": MODEL_NAME, "files_sha256": h.hexdigest()}


def build_index():
    from rank_bm25 import BM25Okapi

    chunks = []
    for md_file in sorted(VAULT_DIR.rglob("*.md")):
        chunks.extend(_chunk_document(md_file))

    tokenized = [c["content"].lower().split() for c in chunks]
    bm25 = BM25Okapi(tokenized)

    model = _get_model()
    texts = [c["content"] for c in chunks]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True, batch_size=64)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_DIR / "bm25.pkl", "wb") as f:
        pickle.dump((bm25, chunks), f)
    np.save(INDEX_DIR / "embeddings.npy", embeddings)
    # Written last, so an interrupted build is never mistaken for a valid one.
    (INDEX_DIR / MANIFEST_FILE).write_text(json.dumps(_vault_fingerprint(), indent=2))

    # stderr, never stdout: stdout carries the MCP stdio JSON-RPC stream.
    print(
        f"Indexed {len(chunks)} chunks from {len(set(c['file_path'] for c in chunks))} pages "
        f"into {INDEX_DIR}.",
        file=sys.stderr,
    )
    return bm25, chunks, embeddings


def _index_is_current() -> bool:
    try:
        manifest = json.loads((INDEX_DIR / MANIFEST_FILE).read_text())
    except (OSError, ValueError):
        return False
    return (
        manifest == _vault_fingerprint()
        and (INDEX_DIR / "bm25.pkl").exists()
        and (INDEX_DIR / "embeddings.npy").exists()
    )


def _load_index():
    global _index_cache
    if _index_cache is not None:
        return _index_cache
    if not _index_is_current():
        _index_cache = build_index()
        return _index_cache
    with open(INDEX_DIR / "bm25.pkl", "rb") as f:
        bm25, chunks = pickle.load(f)
    embeddings = np.load(INDEX_DIR / "embeddings.npy")
    _index_cache = (bm25, chunks, embeddings)
    return _index_cache


def _rrf(rankings: list[list[int]], k: int = 60) -> list[tuple[int, float]]:
    scores: dict[int, float] = {}
    for ranked in rankings:
        for rank, idx in enumerate(ranked):
            scores[idx] = scores.get(idx, 0.0) + 1.0 / (k + rank + 1)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def search(query: str, top_k: int = 5) -> list[dict]:
    bm25, chunks, embeddings = _load_index()
    pool = top_k * 6

    bm25_scores = bm25.get_scores(query.lower().split())
    bm25_ranked = list(np.argsort(bm25_scores)[::-1][:pool])

    model = _get_model()
    q_emb = model.encode([query], convert_to_numpy=True)[0]
    norms = np.linalg.norm(embeddings, axis=1)
    sims = (embeddings @ q_emb) / (norms * np.linalg.norm(q_emb) + 1e-9)
    sem_ranked = list(np.argsort(sims)[::-1][:pool])

    fused = _rrf([bm25_ranked, sem_ranked])

    results = []
    for idx, score in fused[:top_k]:
        c = chunks[idx]
        results.append({
            "page": c["page_title"],
            "section": c["section"],
            "file": c["file_path"],
            "tags": c["tags"],
            "score": round(score, 4),
            "content": c["content"][:1000],
        })
    return results


def get_page(name: str) -> str | None:
    name_lower = name.lower().replace("-", " ").replace("_", " ")
    best_path = None
    best_score = 0.0
    for md_file in VAULT_DIR.rglob("*.md"):
        stem_lower = md_file.stem.lower()
        if name_lower == stem_lower:
            return md_file.read_text(encoding="utf-8")
        query_words = set(name_lower.split())
        file_words = set(stem_lower.split())
        score = len(query_words & file_words) / max(len(query_words | file_words), 1)
        if score > best_score:
            best_score = score
            best_path = md_file
    if best_path and best_score > 0:
        return best_path.read_text(encoding="utf-8")
    return None


# Category for pages that sit directly in the content root rather than in a
# category folder (in the bundled vault: the refactoring techniques).
ROOT_CATEGORY = "Refactoring"


def _content_root() -> Path:
    """The vault root, skipping a lone wrapper folder.

    The bundled vault is md_files/refactoring-python/{Smells,Design Patterns,...}.
    Without skipping the wrapper, every page would get the category
    "refactoring-python" and the category filter would be useless.
    """
    root = VAULT_DIR
    while True:
        entries = [p for p in root.iterdir() if not p.name.startswith(".")]
        dirs = [p for p in entries if p.is_dir()]
        if len(dirs) == 1 and not any(p.suffix == ".md" for p in entries):
            root = dirs[0]
        else:
            return root


def list_catalog(category: str = "all") -> list[dict]:
    pages = []
    root = _content_root()
    for md_file in sorted(VAULT_DIR.rglob("*.md")):
        meta, _ = _parse_frontmatter(md_file.read_text(encoding="utf-8"))
        tags = meta.get("tags", [])
        relative = str(md_file.relative_to(VAULT_DIR))
        parts = md_file.relative_to(root).parts
        cat = parts[0] if len(parts) > 1 else ROOT_CATEGORY
        if category == "all" or category.lower() in cat.lower():
            pages.append({"name": md_file.stem, "category": cat, "file": relative, "tags": tags})
    return pages


def main() -> None:
    """`refactoring-python-mcp-index`: pre-build the index so the first search is fast."""
    parser = argparse.ArgumentParser(
        prog="refactoring-python-mcp-index",
        description="Build the refactoring-python-mcp search index.",
    )
    parser.add_argument("--force", action="store_true", help="rebuild even if the index is current")
    args = parser.parse_args()

    print(f"Vault: {VAULT_DIR}\nIndex: {INDEX_DIR}", file=sys.stderr)
    if not args.force and _index_is_current():
        print("Index is up to date (use --force to rebuild).", file=sys.stderr)
        return
    build_index()


if __name__ == "__main__":
    main()
