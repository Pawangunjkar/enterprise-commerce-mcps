"""MCP server for offer-promotion-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("offer-promotion-service")
client = EcsClient("http://localhost:8108")

@mcp.tool()
def create_offer(payload: dict | None = None) -> dict:
    """Call POST /api/v1/offers."""
    try:
        return client.post("/api/v1/offers", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
