# refactoring-python-mcp

An MCP server that gives AI agents searchable access to a refactoring knowledge base: code smells, refactoring techniques and design patterns, with Python examples. The knowledge base (165 pages) ships inside the package, so you don't need to clone anything to use it.

## Requirements

- [uv](https://docs.astral.sh/uv/) (for `uvx`) or [pipx](https://pipx.pypa.io/)
- Python 3.10 or newer (uv can download one for you)

## Register with Claude Code

```bash
claude mcp add --scope user refactoring-python -- \
  uvx --from git+https://github.com/pogpog/refactoring-python-mcp refactoring-python-mcp
```

Restart Claude Code to pick up the server. Before using it for the first time, read [First run](#first-run).

## Register with other MCP clients

Add this to the client's JSON config:

```json
{
  "mcpServers": {
    "refactoring-python": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/pogpog/refactoring-python-mcp",
        "refactoring-python-mcp"
      ]
    }
  }
}
```

## Other ways to install

Install it permanently with pipx. This puts `refactoring-python-mcp` and `refactoring-python-mcp-index` on your `PATH`:

```bash
pipx install git+https://github.com/pogpog/refactoring-python-mcp
claude mcp add --scope user refactoring-python -- refactoring-python-mcp
```

Run it from a local clone:

```bash
git clone https://github.com/pogpog/refactoring-python-mcp.git
claude mcp add --scope user refactoring-python -- \
  uvx --from /path/to/refactoring-python-mcp refactoring-python-mcp
```

The package is not on PyPI yet. Once it is published, the short forms `uvx refactoring-python-mcp` and `pipx install refactoring-python-mcp` will work.

## First run

The first launch is slow, so do it once before your MCP client needs the server:

- **Install.** `sentence-transformers` pulls in PyTorch. On Linux the default PyTorch wheels include CUDA, which adds up to about 2.5 GB. uv caches the download, so later launches are fast.
- **Index.** The first search downloads the `all-MiniLM-L6-v2` model (~90 MB) and builds the search index, which takes about 20 seconds. An MCP client with a short tool-call timeout may give up on that first call.

To get both out of the way, build the index ahead of time:

```bash
uvx --from git+https://github.com/pogpog/refactoring-python-mcp refactoring-python-mcp-index
```

## Updating

uvx caches the build from GitHub, so it keeps running the version it first installed. To pull the latest commit:

```bash
uvx --refresh-package refactoring-python-mcp \
  --from git+https://github.com/pogpog/refactoring-python-mcp refactoring-python-mcp-index
```

Then restart your MCP client. With pipx, run `pipx upgrade refactoring-python-mcp` instead.

You don't need to delete the index after an update. It is rebuilt automatically if the pages changed (see [Configuration](#configuration)).

## Tools

| Tool | Description |
| --- | --- |
| `search_refactoring(query, top_k)` | Hybrid BM25 + semantic search across all pages. Best for open-ended questions. `top_k` defaults to 5 (max 10). |
| `get_refactoring_page(name)` | Full content of a page by name, e.g. `"Extract Method"`, `"Decorator"`, `"Long Method"`. |
| `list_refactoring_catalog(category)` | List all pages, optionally filtered by category. |

The bundled knowledge base has three categories:

| Category | Pages | Contents |
| --- | --- | --- |
| `Refactoring` | 88 | Refactoring techniques and overview pages |
| `Design Patterns` | 54 | Creational, structural and behavioral patterns |
| `Smells` | 23 | Code smells |

The category filter matches part of a name and ignores case, so `"smell"` and `"pattern"` also work. `"all"` (the default) lists every page.

## Configuration

| Environment variable | Default | Purpose |
| --- | --- | --- |
| `REFACTORING_PYTHON_MCP_VAULT_DIR` | bundled `md_files/` | Folder of markdown files to index, e.g. an Obsidian vault |
| `REFACTORING_PYTHON_MCP_INDEX_DIR` | `$XDG_CACHE_HOME/refactoring-python-mcp` (`~/.cache/refactoring-python-mcp`) | Where the BM25 index and embeddings are stored |

Pass these through your MCP client. For example, with Claude Code:

```bash
claude mcp add --scope user refactoring-python \
  -e REFACTORING_PYTHON_MCP_VAULT_DIR=/path/to/vault \
  -e REFACTORING_PYTHON_MCP_INDEX_DIR=~/.cache/refactoring-python-mcp-myvault \
  -- uvx --from git+https://github.com/pogpog/refactoring-python-mcp refactoring-python-mcp
```

The index stores a fingerprint of the vault's contents and the embedding model. It is rebuilt automatically when the markdown files change, when an update changes the bundled pages, or when you point the server at a different vault. To force a rebuild:

```bash
uvx --from git+https://github.com/pogpog/refactoring-python-mcp refactoring-python-mcp-index --force
```

If you use more than one vault, give each its own `REFACTORING_PYTHON_MCP_INDEX_DIR`. Otherwise they keep overwriting each other's index.

In a custom vault, each page's category is its first folder. If all the pages sit inside one wrapper folder, the folder below it is used. Pages directly in the vault's top folder are listed under `Refactoring`.

## How it works

1. Each markdown file is split into chunks at its `##` headings: 165 pages become 539 chunks.
2. A BM25 index is built over the tokenized chunk text.
3. Each chunk is embedded with [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) via `sentence-transformers`.
4. At query time the BM25 and cosine-similarity rankings are merged with Reciprocal Rank Fusion. Exact keyword matches (`"Extract Method"`) and semantic matches (`"my class is too big"`) therefore both work.

The index is built the first time it is needed and then loaded from disk. It lives outside the package because uvx and pipx can recreate their environments at any time.

## Development

```bash
git clone https://github.com/pogpog/refactoring-python-mcp.git
cd refactoring-python-mcp
uv build                                                                     # dist/*.whl and *.tar.gz
uvx --refresh-package refactoring-python-mcp --from . refactoring-python-mcp   # run local edits
```

Things to know:

- **uvx caches builds of local paths.** Without `--refresh-package`, it keeps running the old code.
- **`mcp` is pinned to `<2`.** mcp 2.0 renamed `FastMCP` to `MCPServer`, so the server would fail at import.
- **Bump the version for every release.** It is in both `pyproject.toml` and `src/refactoring_python_mcp/__init__.py`.
- **Keep stdout clean.** The server communicates with the client over stdout, so log to stderr. A stray `print()` corrupts the protocol.

## Project structure

```text
refactoring-python-mcp/
├── pyproject.toml          # Package metadata, dependencies, console scripts
└── src/
    └── refactoring_python_mcp/
        ├── __init__.py
        ├── server.py       # MCP server: tool definitions, main() entry point
        ├── indexer.py      # Chunking, indexing, hybrid search, refactoring-python-mcp-index CLI
        └── md_files/       # Knowledge base (shipped inside the wheel)
```
