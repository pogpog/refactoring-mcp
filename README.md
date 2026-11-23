# refactoring-mcp

A local MCP server that gives AI agents searchable access to a refactoring knowledge base — code smells, refactoring techniques, and design patterns.

## How it works

Markdown files are stored in `md_files/` in this repo. The server indexes those files using a hybrid search pipeline and exposes the results as MCP tools.

### Indexing pipeline

1. Each markdown file is chunked at `##` headings — 165 pages become ~540 chunks
2. A **BM25** index is built over the tokenized chunk text
3. Each chunk is embedded using [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) via `sentence-transformers`
4. Both the BM25 index and embeddings are persisted to `.index/` so startup is instant

### Search

At query time, both BM25 and cosine similarity rankings are computed independently, then merged using **Reciprocal Rank Fusion (RRF)**. This means exact keyword matches (e.g. `"Extract Method"`) and semantic matches (e.g. `"my class is too big"`) both work well.

## Configuration

By default, `VAULT_DIR` in `indexer.py` points at the bundled `md_files/` folder. To index markdown files stored somewhere else (e.g. an Obsidian vault), change it to that folder:

```python
VAULT_DIR = Path("/path/to/your/md-files")
```

The server will index all `.md` files found recursively under that directory.

## Prerequisites

```bash
pip install mcp rank-bm25 sentence-transformers numpy
```

## Setup

Build the index (only needed once, or after vault files change):

```bash
python3 indexer.py
```

Register with Claude Code:

```bash
claude mcp add --scope user refactoring-python python3 /home/pog/Projects/refactoring-python-mcp/server.py
```

Restart Claude Code to pick up the new server.

## Tools

| Tool | Description |
| --- | --- |
| `search_refactoring(query, top_k)` | Hybrid BM25 + semantic search across all pages. Best for open-ended questions. |
| `get_refactoring_page(name)` | Fetch the full content of a page by name, e.g. `"Extract Method"`, `"Decorator"`. |
| `list_refactoring_catalog(category)` | List all pages, optionally filtered by `"Design Patterns"`, `"Smells"`, or `"Refactoring"`. |

## Rebuilding the index

Delete `.index/` and re-run `indexer.py` whenever the vault files change:

```bash
rm -rf .index && python3 indexer.py
```

## Project structure

```
refactoring-python-mcp/
├── server.py       # MCP server — tool definitions
├── indexer.py      # Chunking, indexing, and hybrid search logic
├── md_files/       # Knowledge base markdown pages
└── .index/         # Persisted BM25 + embeddings (auto-generated)
```
