"""MCP server for loyalty-rewards-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("loyalty-rewards-service")
client = EcsClient("http://localhost:8406")

@mcp.tool()
def get_loyalty(customerId: str = "", festivalMultiplier: float = 1.0) -> dict:
    """Call GET /api/v1/loyalty/{customerId}."""
    try:
        return client.request("GET", f"/api/v1/loyalty/{customerId}", params={ "festivalMultiplier": festivalMultiplier })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
