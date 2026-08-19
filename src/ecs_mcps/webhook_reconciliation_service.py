"""MCP server for webhook-reconciliation-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("webhook-reconciliation-service")
client = EcsClient("http://localhost:8308")

@mcp.tool()
def ingest_webhook(provider: str = "") -> dict:
    """Call POST /api/v1/payments/webhooks/{provider}."""
    try:
        return client.request("POST", f"/api/v1/payments/webhooks/{provider}")
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
