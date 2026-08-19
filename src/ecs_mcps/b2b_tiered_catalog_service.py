"""MCP server for b2b-tiered-catalog-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("b2b-tiered-catalog-service")
client = EcsClient("http://localhost:8104")

@mcp.tool()
def b2b_quote(payload: dict | None = None) -> dict:
    """Call POST /api/v1/catalog/b2b/quote."""
    try:
        return client.post("/api/v1/catalog/b2b/quote", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
