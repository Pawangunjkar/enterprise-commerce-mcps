"""MCP server for serial-imei-tracking-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("serial-imei-tracking-service")
client = EcsClient("http://localhost:8103")

@mcp.tool()
def ingest_imei(sku: str = "", imei1: str = "", imei2: str = "", serial: str = "") -> dict:
    """Call POST /api/v1/imei/ingest."""
    try:
        return client.request("POST", "/api/v1/imei/ingest", json={ "sku": sku, "imei1": imei1, "imei2": imei2, "serial": serial })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
