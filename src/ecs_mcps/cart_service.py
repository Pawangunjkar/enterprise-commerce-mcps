"""MCP server for cart-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("cart-service")
client = EcsClient("http://localhost:8201")

@mcp.tool()
def get_cart(cartId: str = "") -> dict:
    """Call GET /api/v1/carts/{cartId}."""
    try:
        return client.request("GET", f"/api/v1/carts/{cartId}")
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def add_cart_item(cartId: str = "", sku: str = "", qty: int = 0, unitPrice: float = 0.0) -> dict:
    """Call POST /api/v1/carts/{cartId}/items."""
    try:
        return client.request("POST", f"/api/v1/carts/{cartId}/items", json={ "sku": sku, "qty": qty, "unitPrice": unitPrice })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
