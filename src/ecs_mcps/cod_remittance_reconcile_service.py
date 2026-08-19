"""MCP server for cod-remittance-reconcile-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("cod-remittance-reconcile-service")
client = EcsClient("http://localhost:8307")

@mcp.tool()
def match_cod(awb: str = "", carrierAmount: float = 0.0, bankAmount: float = 0.0) -> dict:
    """Call POST /api/v1/cod/match."""
    try:
        return client.request("POST", "/api/v1/cod/match", json={ "awb": awb, "carrierAmount": carrierAmount, "bankAmount": bankAmount })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
