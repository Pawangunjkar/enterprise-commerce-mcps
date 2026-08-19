"""MCP server for cart-abandonment-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("cart-abandonment-service")
client = EcsClient("http://localhost:8407")

@mcp.tool()
def mark_abandoned(payload: dict | None = None) -> dict:
    """Call POST /api/v1/carts/abandonment."""
    try:
        return client.post("/api/v1/carts/abandonment", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
