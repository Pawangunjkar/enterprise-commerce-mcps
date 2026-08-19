"""MCP server for invoice-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("invoice-service")
client = EcsClient("http://localhost:8309")

@mcp.tool()
def issue_invoice(payload: dict | None = None) -> dict:
    """Call POST /api/v1/invoices."""
    try:
        return client.post("/api/v1/invoices", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
