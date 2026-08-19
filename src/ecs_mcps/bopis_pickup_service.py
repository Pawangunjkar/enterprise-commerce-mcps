"""MCP server for bopis-pickup-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("bopis-pickup-service")
client = EcsClient("http://localhost:8209")

@mcp.tool()
def reserve_pickup(payload: dict | None = None) -> dict:
    """Call POST /api/v1/bopis/reservations."""
    try:
        return client.post("/api/v1/bopis/reservations", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
