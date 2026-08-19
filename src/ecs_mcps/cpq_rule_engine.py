"""MCP server for cpq-rule-engine."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("cpq-rule-engine")
client = EcsClient("http://localhost:8106")

@mcp.tool()
def evaluate_cpq(payload: dict | None = None) -> dict:
    """Call POST /api/v1/catalog/cpq/evaluate."""
    try:
        return client.post("/api/v1/catalog/cpq/evaluate", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
