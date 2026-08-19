"""MCP server for product-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("product-service")
client = EcsClient("http://localhost:8101")

@mcp.tool()
def list_products(page: int = 0, size: int = 20) -> dict:
    """Call GET /api/v1/products."""
    try:
        return client.request("GET", "/api/v1/products", params={ "page": page, "size": size })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def get_product(id: str = "") -> dict:
    """Call GET /api/v1/products/{id}."""
    try:
        return client.request("GET", f"/api/v1/products/{id}")
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def create_product(sku: str = "", name: str = "", hsnCode: str = "", brand: str | None = "", categoryPath: str = "", listPriceInr: float = 0.0) -> dict:
    """Call POST /api/v1/products."""
    try:
        return client.request("POST", "/api/v1/products", json={ "sku": sku, "name": name, "hsnCode": hsnCode, "brand": brand, "categoryPath": categoryPath, "listPriceInr": listPriceInr })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def activate_product(id: str = "") -> dict:
    """Call PUT /api/v1/products/{id}/activate."""
    try:
        return client.request("PUT", f"/api/v1/products/{id}/activate")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
