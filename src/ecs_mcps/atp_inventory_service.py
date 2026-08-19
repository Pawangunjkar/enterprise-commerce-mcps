"""MCP server for atp-inventory-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("atp-inventory-service")
client = EcsClient("http://localhost:8205")

@mcp.tool()
def lock_stock(sku: str = "", qty: int = 0, warehouse: str = "DEL-FC-01") -> dict:
    """Call POST /api/v1/inventory/lock."""
    try:
        return client.request("POST", "/api/v1/inventory/lock", json={ "sku": sku, "qty": qty, "warehouse": warehouse })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
