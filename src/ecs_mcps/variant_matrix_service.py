"""MCP server for variant-matrix-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("variant-matrix-service")
client = EcsClient("http://localhost:8102")

@mcp.tool()
def explode_variants(payload: dict | None = None) -> dict:
    """Call POST /api/v1/catalog/variants/explode."""
    try:
        return client.post("/api/v1/catalog/variants/explode", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
