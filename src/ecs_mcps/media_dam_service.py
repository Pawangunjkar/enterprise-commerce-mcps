"""MCP server for media-dam-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("media-dam-service")
client = EcsClient("http://localhost:8110")

@mcp.tool()
def health() -> dict:
    """Call GET /actuator/health."""
    try:
        return client.request("GET", "/actuator/health")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
