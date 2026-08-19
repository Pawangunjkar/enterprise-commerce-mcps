"""MCP server for ecommerce-storefront-portal."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("ecommerce-storefront-portal")
client = EcsClient("http://localhost:8080")

@mcp.tool()
def search_store(q: str = "*:*", brand: str | None = None, start: int = 0, rows: int = 20) -> dict:
    """Call GET /api/v1/search/products."""
    try:
        return client.request("GET", "/api/v1/search/products", params={ "q": q, "brand": brand, "start": start, "rows": rows })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def check_edd(pincode: str = "") -> dict:
    """Call GET /api/v1/pincodes/{pincode}/serviceability."""
    try:
        return client.request("GET", f"/api/v1/pincodes/{pincode}/serviceability")
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def create_upi_qr(orderId: str = "", amount: float = 0.0, vpa: str = "ecs@upi", merchantName: str = "ECS Store", mcc: str = "") -> dict:
    """Call POST /api/v1/payments/upi/bharat-qr."""
    try:
        return client.request("POST", "/api/v1/payments/upi/bharat-qr", json={ "orderId": orderId, "amount": amount, "vpa": vpa, "merchantName": merchantName, "mcc": mcc })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
