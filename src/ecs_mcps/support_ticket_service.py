"""MCP server for support-ticket-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("support-ticket-service")
client = EcsClient("http://localhost:8405")

@mcp.tool()
def create_ticket(payload: dict | None = None) -> dict:
    """Call POST /api/v1/tickets."""
    try:
        return client.post("/api/v1/tickets", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
