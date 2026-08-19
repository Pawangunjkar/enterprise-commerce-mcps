"""MCP server for subscription-emi-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("subscription-emi-service")
client = EcsClient("http://localhost:8304")

@mcp.tool()
def emi_quote(principal: float = 24999.0, months: int = 0) -> dict:
    """Call GET /api/v1/emi/quote."""
    try:
        return client.request("GET", "/api/v1/emi/quote", params={ "principal": principal, "months": months })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
