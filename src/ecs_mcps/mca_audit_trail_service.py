"""MCP server for mca-audit-trail-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("mca-audit-trail-service")
client = EcsClient("http://localhost:8093")

@mcp.tool()
def append_audit(actor: str = "", action: str = "REATTEMPT", resourceType: str = "ORDER", resourceId: str = "") -> dict:
    """Call POST /api/v1/audit."""
    try:
        return client.request("POST", "/api/v1/audit", json={ "actor": actor, "action": action, "resourceType": resourceType, "resourceId": resourceId })
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
