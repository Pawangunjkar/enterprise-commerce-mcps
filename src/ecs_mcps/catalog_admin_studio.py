"""MCP server for catalog-admin-studio."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("catalog-admin-studio")
client = EcsClient("http://localhost:8080")

@mcp.tool()
def list_products(page: int = 0, size: int = 20) -> dict:
    """Call GET /api/v1/products."""
    try:
        return client.request("GET", "/api/v1/products", params={ "page": page, "size": size })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def ingest_imei(sku: str = "", imei1: str = "", imei2: str = "", serial: str = "") -> dict:
    """Call POST /api/v1/imei/ingest."""
    try:
        return client.request("POST", "/api/v1/imei/ingest", json={ "sku": sku, "imei1": imei1, "imei2": imei2, "serial": serial })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def time_travel(asOf: str = "") -> dict:
    """Call GET /api/v1/catalog/time-travel."""
    try:
        return client.request("GET", "/api/v1/catalog/time-travel", params={ "asOf": asOf })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
