"""MCP server for order-orchestrator."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("order-orchestrator")
client = EcsClient("http://localhost:8203")

@mcp.tool()
def place_order(cartId: str = "", pincode: str = "", paymentMode: str = "UPI", amount: float = 0.0) -> dict:
    """Call POST /api/v1/orders."""
    try:
        return client.request("POST", "/api/v1/orders", json={ "cartId": cartId, "pincode": pincode, "paymentMode": paymentMode, "amount": amount })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
