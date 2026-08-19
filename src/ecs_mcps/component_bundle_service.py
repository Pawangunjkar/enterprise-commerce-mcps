"""MCP server for component-bundle-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("component-bundle-service")
client = EcsClient("http://localhost:8105")

@mcp.tool()
def price_bundle(payload: dict | None = None) -> dict:
    """Call POST /api/v1/catalog/bundles/price."""
    try:
        return client.post("/api/v1/catalog/bundles/price", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
