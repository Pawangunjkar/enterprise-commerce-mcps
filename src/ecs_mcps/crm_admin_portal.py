"""MCP server for crm-admin-portal."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("crm-admin-portal")
client = EcsClient("http://localhost:8080")

@mcp.tool()
def otp_start(mobile: str = "") -> dict:
    """Call POST /api/v1/customers/otp/start."""
    try:
        return client.request("POST", "/api/v1/customers/otp/start", json={ "mobile": mobile })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def create_ticket(payload: dict | None = None) -> dict:
    """Call POST /api/v1/tickets."""
    try:
        return client.post("/api/v1/tickets", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def account_tree() -> dict:
    """Call GET /api/v1/accounts/tree."""
    try:
        return client.request("GET", "/api/v1/accounts/tree")
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def record_consent(payload: dict | None = None) -> dict:
    """Call POST /api/v1/dpdp/consent."""
    try:
        return client.post("/api/v1/dpdp/consent", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
