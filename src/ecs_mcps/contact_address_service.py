"""MCP server for contact-address-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("contact-address-service")
client = EcsClient("http://localhost:8404")

@mcp.tool()
def autofill_address(pincode: str = "") -> dict:
    """Call GET /api/v1/addresses/autofill."""
    try:
        return client.request("GET", "/api/v1/addresses/autofill", params={ "pincode": pincode })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
