"""MCP server for order-admin-portal."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("order-admin-portal")
client = EcsClient("http://localhost:8080")

@mcp.tool()
def place_order(cartId: str = "", pincode: str = "", paymentMode: str = "UPI", amount: float = 0.0) -> dict:
    """Call POST /api/v1/orders."""
    try:
        return client.request("POST", "/api/v1/orders", json={ "cartId": cartId, "pincode": pincode, "paymentMode": paymentMode, "amount": amount })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def create_wave(payload: dict | None = None) -> dict:
    """Call POST /api/v1/wms/waves."""
    try:
        return client.post("/api/v1/wms/waves", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


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
