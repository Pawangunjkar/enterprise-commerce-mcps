"""MCP server for ondc-seller-gateway."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("ondc-seller-gateway")
client = EcsClient("http://localhost:8207")

@mcp.tool()
def beckn_search(payload: dict | None = None) -> dict:
    """Call POST /ondc/search."""
    try:
        return client.post("/ondc/search", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def beckn_select(payload: dict | None = None) -> dict:
    """Call POST /ondc/select."""
    try:
        return client.post("/ondc/select", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def beckn_init(payload: dict | None = None) -> dict:
    """Call POST /ondc/init."""
    try:
        return client.post("/ondc/init", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def beckn_confirm(payload: dict | None = None) -> dict:
    """Call POST /ondc/confirm."""
    try:
        return client.post("/ondc/confirm", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def beckn_status(payload: dict | None = None) -> dict:
    """Call POST /ondc/status."""
    try:
        return client.post("/ondc/status", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def beckn_track(payload: dict | None = None) -> dict:
    """Call POST /ondc/track."""
    try:
        return client.post("/ondc/track", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def beckn_cancel(payload: dict | None = None) -> dict:
    """Call POST /ondc/cancel."""
    try:
        return client.post("/ondc/cancel", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
