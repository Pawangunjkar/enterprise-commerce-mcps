"""MCP server for billing-admin-portal."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("billing-admin-portal")
client = EcsClient("http://localhost:8080")

@mcp.tool()
def compute_gst(taxable: float = 0.0, slab: int = 18, originState: str = "HR", destState: str = "MH", hsn: str = "") -> dict:
    """Call POST /api/v1/gst/compute."""
    try:
        return client.request("POST", "/api/v1/gst/compute", json={ "taxable": taxable, "slab": slab, "originState": originState, "destState": destState, "hsn": hsn })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def compute_tcs_194o(payload: dict | None = None) -> dict:
    """Call POST /api/v1/tcs/194o."""
    try:
        return client.post("/api/v1/tcs/194o", json=payload or {})
    except Exception as exc:
        return {"error": str(exc)}


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
