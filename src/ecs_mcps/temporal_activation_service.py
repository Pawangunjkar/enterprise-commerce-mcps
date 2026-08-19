"""MCP server for temporal-activation-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("temporal-activation-service")
client = EcsClient("http://localhost:8109")

@mcp.tool()
def time_travel(asOf: str = "") -> dict:
    """Call GET /api/v1/catalog/time-travel."""
    try:
        return client.request("GET", "/api/v1/catalog/time-travel", params={ "asOf": asOf })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
