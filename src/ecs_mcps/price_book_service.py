"""MCP server for price-book-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("price-book-service")
client = EcsClient("http://localhost:8303")

@mcp.tool()
def get_price_book(sku: str = "") -> dict:
    """Call GET /api/v1/price-books/{sku}."""
    try:
        return client.request("GET", f"/api/v1/price-books/{sku}")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
