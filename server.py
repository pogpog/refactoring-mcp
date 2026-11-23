from mcp.server.fastmcp import FastMCP
import indexer

mcp = FastMCP("refactoring-python")


@mcp.tool()
def search_refactoring(query: str, top_k: int = 5) -> str:
    """Search the refactoring knowledge base using hybrid BM25 + semantic search.
    Returns relevant chunks about code smells, refactoring techniques, and design patterns.
    Use this when you need guidance on how to refactor code or identify a design pattern.

    Args:
        query: Natural language query, e.g. "how to fix a long method", "decorator pattern"
        top_k: Number of results to return (default 5, max 10)
    """
    results = indexer.search(query, top_k=min(top_k, 10))
    if not results:
        return "No results found."

    lines = []
    for i, r in enumerate(results, 1):
        section_str = f" › {r['section']}" if r['section'] else ""
        lines.append(f"### {i}. {r['page']}{section_str}")
        lines.append(f"**File:** `{r['file']}`  **Tags:** {', '.join(r['tags'])}")
        lines.append("")
        lines.append(r["content"])
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def get_refactoring_page(name: str) -> str:
    """Retrieve the full content of a specific knowledge base page by name.
    Use this when you know exactly which page you need.

    Args:
        name: Page name, e.g. "Extract Method", "Decorator", "Long Method", "Large Class"
    """
    content = indexer.get_page(name)
    if content is None:
        return f"Page '{name}' not found. Try search_refactoring to discover available pages."
    return content


@mcp.tool()
def list_refactoring_catalog(category: str = "all") -> str:
    """List all pages in the refactoring knowledge base, optionally filtered by category.

    Args:
        category: Filter by category. Options: "all", "Design Patterns", "Smells", "Refactoring". Default: "all"
    """
    pages = indexer.list_catalog(category)
    if not pages:
        return f"No pages found for category '{category}'."

    by_cat: dict[str, list[str]] = {}
    for p in pages:
        by_cat.setdefault(p["category"], []).append(p["name"])

    lines = [f"## Refactoring Catalog ({len(pages)} pages)\n"]
    for cat, names in sorted(by_cat.items()):
        lines.append(f"### {cat} ({len(names)})")
        for name in names:
            lines.append(f"- {name}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
