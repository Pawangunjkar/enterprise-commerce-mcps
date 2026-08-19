"""MCP server for dunning-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("dunning-service")
client = EcsClient("http://localhost:8311")

@mcp.tool()
def dunning_schedule() -> dict:
    """Call GET /api/v1/dunning/schedule."""
    try:
        return client.request("GET", "/api/v1/dunning/schedule")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
