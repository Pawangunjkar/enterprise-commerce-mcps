"""MCP server for gst-tax-engine."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("gst-tax-engine")
client = EcsClient("http://localhost:8301")

@mcp.tool()
def compute_gst(taxable: float = 0.0, slab: int = 18, originState: str = "HR", destState: str = "MH", hsn: str = "") -> dict:
    """Call POST /api/v1/gst/compute."""
    try:
        return client.request("POST", "/api/v1/gst/compute", json={ "taxable": taxable, "slab": slab, "originState": originState, "destState": destState, "hsn": hsn })
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def eway_bill(taxable: float = 0.0, slab: int = 18, originState: str = "HR", destState: str = "MH", hsn: str = "") -> dict:
    """Call POST /api/v1/gst/eway-bill."""
    try:
        return client.request("POST", "/api/v1/gst/eway-bill", json={ "taxable": taxable, "slab": slab, "originState": originState, "destState": destState, "hsn": hsn })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
