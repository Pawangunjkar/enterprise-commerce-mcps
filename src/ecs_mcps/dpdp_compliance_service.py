"""MCP server for dpdp-compliance-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("dpdp-compliance-service")
client = EcsClient("http://localhost:8408")

@mcp.tool()
def record_consent(payload: dict | None = None) -> dict:
    """Call POST /api/v1/dpdp/consent."""
    try:
        return client.post("/api/v1/dpdp/consent", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def anonymize_customer(customerId: str = "") -> dict:
    """Call POST /api/v1/dpdp/anonymize/{customerId}."""
    try:
        return client.request("POST", f"/api/v1/dpdp/anonymize/{customerId}")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
