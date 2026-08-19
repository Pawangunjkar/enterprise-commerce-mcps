"""MCP server for dynamic-price-engine."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("dynamic-price-engine")
client = EcsClient("http://localhost:8204")

@mcp.tool()
def calculate_price(sku: str = "", basePrice: float = 0.0, offerDiscount: float = 0.0, loyaltyDiscount: float = 0.0) -> dict:
    """Call POST /api/v1/prices/calculate."""
    try:
        return client.request("POST", "/api/v1/prices/calculate", json={ "sku": sku, "basePrice": basePrice, "offerDiscount": offerDiscount, "loyaltyDiscount": loyaltyDiscount })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
