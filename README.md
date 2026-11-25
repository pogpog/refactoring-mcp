# refactoring-python-mcp

An MCP server that gives AI agents searchable access to a refactoring knowledge base: code smells, refactoring techniques and design patterns. You can install it with `uvx` or `pipx`.

## Install and run

From a local checkout:

```bash
uvx --from /path/to/refactoring-python-mcp refactoring-python-mcp
```

From git (once pushed):

```bash
uvx --from git+https://github.com/<owner>/<repo> refactoring-python-mcp
pipx install git+https://github.com/<owner>/<repo>
```

From PyPI (once published):

```bash
uvx refactoring-python-mcp
pipx install refactoring-python-mcp
```

## Register with an MCP client

Claude Code:

```bash
claude mcp add --scope user refactoring -- uvx refactoring-python-mcp
```

Any MCP client's JSON config:

```json
{
  "mcpServers": {
    "refactoring": { "command": "uvx", "args": ["refactoring-python-mcp"] }
  }
}
```

Until it is on PyPI, use `"args": ["--from", "/path/or/git+url", "refactoring-python-mcp"]`.

## First run

The first install downloads PyTorch (via `sentence-transformers`), which is several hundred MB. The first search also downloads the `all-MiniLM-L6-v2` model (~90 MB) and builds the index. That first tool call can take a minute, and an MCP client with a short tool-call timeout may give up on it. To avoid this, build the index once before you register the server:

```bash
uvx --from <source> refactoring-python-mcp-index
```

## Configuration

| Environment variable | Default | Purpose |
| --- | --- | --- |
| `REFACTORING_PYTHON_MCP_VAULT_DIR` | bundled `md_files/` | Folder of markdown files to index, e.g. an Obsidian vault |
| `REFACTORING_PYTHON_MCP_INDEX_DIR` | `$XDG_CACHE_HOME/refactoring-python-mcp` (`~/.cache/refactoring-python-mcp`) | Where the BM25 index and embeddings are stored |

The index records a fingerprint of the vault's contents and the embedding model. It is rebuilt automatically when the markdown files change, when you upgrade to a version whose pages differ, or when you point the server at a different vault. To force a rebuild:

```bash
uvx --from <source> refactoring-python-mcp-index --force
```

If you use more than one vault, give each its own `REFACTORING_PYTHON_MCP_INDEX_DIR`. Otherwise they keep overwriting each other's index.

## How it works

1. Each markdown file is split into chunks at its `##` headings: 165 pages become ~540 chunks.
2. A BM25 index is built over the tokenized chunk text.
3. Each chunk is embedded with [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).
4. At query time the BM25 and cosine-similarity rankings are merged with Reciprocal Rank Fusion. Exact keyword matches (`"Extract Method"`) and semantic matches (`"my class is too big"`) therefore both work.

## Tools

| Tool | Description |
| --- | --- |
| `search_refactoring(query, top_k)` | Hybrid BM25 + semantic search across all pages. |
| `get_refactoring_page(name)` | Full content of a page by name, e.g. `"Extract Method"`, `"Decorator"`. |
| `list_refactoring_catalog(category)` | List all pages, optionally filtered by category. |

## Development

```bash
uv build                                                         # dist/*.whl and *.tar.gz
uvx --refresh-package refactoring-python-mcp --from . refactoring-python-mcp   # rebuild after local edits
```

uvx caches builds of local paths, so without `--refresh-package` it keeps running the old code. Note that `mcp` is pinned to `<2`: mcp 2.0 renamed `FastMCP` to `MCPServer`, and the server would fail at import.

Bump `version` in `pyproject.toml` (and `src/refactoring_python_mcp/__init__.py`) for every release. uvx caches by version.

## Project structure

```text
refactoring-python-mcp/
├── pyproject.toml
└── src/
    └── refactoring_python_mcp/
        ├── __init__.py
        ├── server.py       # MCP server: tool definitions, main() entry point
        ├── indexer.py      # Chunking, indexing, hybrid search, refactoring-python-mcp-index CLI
        └── md_files/       # Knowledge base (shipped inside the wheel)
```
