"""MCP server for wms-fulfillment-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("wms-fulfillment-service")
client = EcsClient("http://localhost:8206")

@mcp.tool()
def create_wave(payload: dict | None = None) -> dict:
    """Call POST /api/v1/wms/waves."""
    try:
        return client.post("/api/v1/wms/waves", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
