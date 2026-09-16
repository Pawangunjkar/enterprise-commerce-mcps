"""MCP server for customer-360-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("customer-360-service")
client = EcsClient("http://localhost:8401")

@mcp.tool()
def otp_start(mobile: str = "") -> dict:
    """Call POST /api/v1/customers/otp/start."""
    try:
        return client.request("POST", "/api/v1/customers/otp/start", json={ "mobile": mobile })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def otp_verify(mobile: str = "", otp: str = "") -> dict:
    """Call POST /api/v1/customers/otp/verify."""
    try:
        return client.request("POST", "/api/v1/customers/otp/verify", json={ "mobile": mobile, "otp": otp })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def upsert_profile(mobile: str = "", pan: str = "", gstin: str = "", name: str = "") -> dict:
    """Call PUT /api/v1/customers/{mobile}."""
    try:
        return client.request("PUT", f"/api/v1/customers/{mobile}", json={ "pan": pan, "gstin": gstin, "name": name })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def get_profile(mobile: str = "") -> dict:
    """Call GET /api/v1/customers/{mobile}."""
    try:
        return client.request("GET", f"/api/v1/customers/{mobile}")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
