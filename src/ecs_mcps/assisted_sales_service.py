"""MCP server for assisted-sales-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("assisted-sales-service")
client = EcsClient("http://localhost:8402")

@mcp.tool()
def create_paylink(payload: dict | None = None) -> dict:
    """Call POST /api/v1/assisted-sales/paylinks."""
    try:
        return client.post("/api/v1/assisted-sales/paylinks", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
