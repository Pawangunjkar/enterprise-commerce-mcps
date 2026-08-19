"""MCP server for payment-gateway-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("payment-gateway-service")
client = EcsClient("http://localhost:8305")

@mcp.tool()
def create_bharat_qr(orderId: str = "", amount: float = 0.0, vpa: str = "ecs@upi", merchantName: str = "ECS Store", mcc: str = "") -> dict:
    """Call POST /api/v1/payments/upi/bharat-qr."""
    try:
        return client.request("POST", "/api/v1/payments/upi/bharat-qr", json={ "orderId": orderId, "amount": amount, "vpa": vpa, "merchantName": merchantName, "mcc": mcc })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def payment_status(txnId: str = "") -> dict:
    """Call GET /api/v1/payments/{txnId}/status."""
    try:
        return client.request("GET", f"/api/v1/payments/{txnId}/status")
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def simulate_success(txnId: str = "") -> dict:
    """Call POST /api/v1/payments/{txnId}/simulate-success."""
    try:
        return client.request("POST", f"/api/v1/payments/{txnId}/simulate-success")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
