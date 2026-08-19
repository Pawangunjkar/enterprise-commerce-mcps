"""MCP server for master-admin-portal."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("master-admin-portal")
client = EcsClient("http://localhost:8080")

@mcp.tool()
def list_dlq(status: str = "OPEN", page: int = 0, size: int = 20) -> dict:
    """Call GET /api/v1/dlq."""
    try:
        return client.request("GET", "/api/v1/dlq", params={ "status": status, "page": page, "size": size })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def replay_dlq(id: str = "") -> dict:
    """Call POST /api/v1/dlq/{id}/replay."""
    try:
        return client.request("POST", f"/api/v1/dlq/{id}/replay")
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def list_audit(resourceType: str = "ORDER", page: int = 0, size: int = 20) -> dict:
    """Call GET /api/v1/audit."""
    try:
        return client.request("GET", "/api/v1/audit", params={ "resourceType": resourceType, "page": page, "size": size })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
