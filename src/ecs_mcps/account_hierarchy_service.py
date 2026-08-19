"""MCP server for account-hierarchy-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("account-hierarchy-service")
client = EcsClient("http://localhost:8403")

@mcp.tool()
def account_tree() -> dict:
    """Call GET /api/v1/accounts/tree."""
    try:
        return client.request("GET", "/api/v1/accounts/tree")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
