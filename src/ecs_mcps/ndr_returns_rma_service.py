"""MCP server for ndr-returns-rma-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("ndr-returns-rma-service")
client = EcsClient("http://localhost:8210")

@mcp.tool()
def ndr_action(awb: str = "", action: str = "REATTEMPT") -> dict:
    """Call POST /api/v1/ndr/{awb}/action."""
    try:
        return client.request("POST", f"/api/v1/ndr/{awb}/action", params={ "action": action })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
