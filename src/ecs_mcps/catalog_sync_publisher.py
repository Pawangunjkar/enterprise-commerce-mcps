"""MCP server for catalog-sync-publisher."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("catalog-sync-publisher")
client = EcsClient("http://localhost:8112")

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
