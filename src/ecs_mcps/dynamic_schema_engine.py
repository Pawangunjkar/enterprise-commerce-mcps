"""MCP server for dynamic-schema-engine."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("dynamic-schema-engine")
client = EcsClient("http://localhost:8107")

@mcp.tool()
def validate_schema(payload: dict | None = None) -> dict:
    """Call POST /api/v1/catalog/schema/validate."""
    try:
        return client.post("/api/v1/catalog/schema/validate", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
