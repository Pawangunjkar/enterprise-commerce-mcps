"""MCP server for general-ledger-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("general-ledger-service")
client = EcsClient("http://localhost:8310")

@mcp.tool()
def post_journal(payload: dict | None = None) -> dict:
    """Call POST /api/v1/ledger/journals."""
    try:
        return client.post("/api/v1/ledger/journals", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
