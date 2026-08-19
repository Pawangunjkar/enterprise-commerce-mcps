"""MCP server for checkout-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("checkout-service")
client = EcsClient("http://localhost:8202")

@mcp.tool()
def create_checkout_intent(cartId: str = "", pincode: str = "", paymentMode: str = "UPI", amount: float = 0.0, gstin: str = "") -> dict:
    """Call POST /api/v1/checkout/intent."""
    try:
        return client.request("POST", "/api/v1/checkout/intent", json={ "cartId": cartId, "pincode": pincode, "paymentMode": paymentMode, "amount": amount, "gstin": gstin })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
