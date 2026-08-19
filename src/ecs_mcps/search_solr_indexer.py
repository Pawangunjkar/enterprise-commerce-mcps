"""MCP server for search-solr-indexer."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("search-solr-indexer")
client = EcsClient("http://localhost:8090")

@mcp.tool()
def search_products(q: str = "*:*", brand: str | None = None, ram: int | None = 0, color: str | None = None, minPrice: float | None = None, maxPrice: float | None = None, start: int = 0, rows: int = 20) -> dict:
    """Call GET /api/v1/search/products."""
    try:
        return client.request("GET", "/api/v1/search/products", params={ "q": q, "brand": brand, "ram": ram, "color": color, "minPrice": minPrice, "maxPrice": maxPrice, "start": start, "rows": rows })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def autocomplete(q: str = "*:*") -> dict:
    """Call GET /api/v1/search/autocomplete."""
    try:
        return client.request("GET", "/api/v1/search/autocomplete", params={ "q": q })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
