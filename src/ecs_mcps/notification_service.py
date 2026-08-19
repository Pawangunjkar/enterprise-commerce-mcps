"""MCP server for notification-service."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("notification-service")
client = EcsClient("http://localhost:8094")

@mcp.tool()
def send_notification(channel: str = "SMS", to: str = "", template: str = "otp") -> dict:
    """Call POST /api/v1/notifications."""
    try:
        return client.request("POST", "/api/v1/notifications", json={ "channel": channel, "to": to, "template": template })
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
