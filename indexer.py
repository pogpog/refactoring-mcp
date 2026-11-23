import re
import pickle
from pathlib import Path
import numpy as np

VAULT_DIR = Path(__file__).parent / "md_files"
INDEX_DIR = Path(__file__).parent / ".index"
MODEL_NAME = "all-MiniLM-L6-v2"

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

    INDEX_DIR.mkdir(exist_ok=True)
    with open(INDEX_DIR / "bm25.pkl", "wb") as f:
        pickle.dump((bm25, chunks), f)
    np.save(INDEX_DIR / "embeddings.npy", embeddings)

    print(f"Indexed {len(chunks)} chunks from {len(set(c['file_path'] for c in chunks))} pages.")
    return bm25, chunks, embeddings


def _load_index():
    global _index_cache
    if _index_cache is not None:
        return _index_cache
    if not (INDEX_DIR / "bm25.pkl").exists():
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


def list_catalog(category: str = "all") -> list[dict]:
    pages = []
    for md_file in sorted(VAULT_DIR.rglob("*.md")):
        meta, _ = _parse_frontmatter(md_file.read_text(encoding="utf-8"))
        tags = meta.get("tags", [])
        relative = str(md_file.relative_to(VAULT_DIR))
        parts = md_file.relative_to(VAULT_DIR).parts
        cat = parts[0] if len(parts) > 1 else "General"
        if category == "all" or category.lower() in cat.lower():
            pages.append({"name": md_file.stem, "category": cat, "file": relative, "tags": tags})
    return pages


if __name__ == "__main__":
    build_index()
