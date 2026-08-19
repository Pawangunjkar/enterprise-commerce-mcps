"""MCP server for pincode-master-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("pincode-master-service")
client = EcsClient("http://localhost:8091")

@mcp.tool()
def get_pincode(pincode: str = "") -> dict:
    """Call GET /api/v1/pincodes/{pincode}."""
    try:
        return client.request("GET", f"/api/v1/pincodes/{pincode}")
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def serviceability(pincode: str = "", origin: str = "110001") -> dict:
    """Call GET /api/v1/pincodes/{pincode}/serviceability."""
    try:
        return client.request("GET", f"/api/v1/pincodes/{pincode}/serviceability", params={ "origin": origin })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
