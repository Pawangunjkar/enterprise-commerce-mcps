"""MCP server for carrier-logistics-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("carrier-logistics-service")
client = EcsClient("http://localhost:8208")

@mcp.tool()
def check_serviceability(carrier: str, payload: dict | None = None) -> dict:
    """Call POST /api/v1/logistics/{carrier}/serviceability."""
    try:
        return client.request("POST", f"/api/v1/logistics/{carrier}/serviceability", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def create_waybill(carrier: str, payload: dict | None = None) -> dict:
    """Call POST /api/v1/logistics/{carrier}/waybills."""
    try:
        return client.request("POST", f"/api/v1/logistics/{carrier}/waybills", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
