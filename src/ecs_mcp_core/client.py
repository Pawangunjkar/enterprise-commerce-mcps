"""Shared HTTP client for Enterprise Commerce MCP servers.

Owner: Pawan Gunjkar <pawangunjkar@gmail.com>
"""

from __future__ import annotations

import os
from typing import Any

import httpx


class EcsHttpError(RuntimeError):
    def __init__(self, status: int, body: str, url: str) -> None:
        super().__init__(f"{status} {url}: {body[:500]}")
        self.status = status
        self.body = body
        self.url = url


class EcsClient:
    def __init__(self, default_base: str) -> None:
        self.base_url = os.environ.get("ECS_SERVICE_URL", os.environ.get("ECS_GATEWAY_URL", default_base)).rstrip("/")
        self.timeout = float(os.environ.get("ECS_HTTP_TIMEOUT", "20"))
        self.headers = {
            "Accept": "application/json",
            "X-Tenant-Id": os.environ.get("ECS_TENANT_ID", "default"),
        }
        token = os.environ.get("ECS_BEARER_TOKEN")
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        with httpx.Client(timeout=self.timeout, headers=self.headers) as client:
            response = client.request(method, url, params=_clean(params), json=json)
        if response.status_code >= 400:
            raise EcsHttpError(response.status_code, response.text, url)
        if not response.content:
            return {"ok": True, "status": response.status_code}
        ctype = response.headers.get("content-type", "")
        if "json" in ctype:
            return response.json()
        return {"ok": True, "status": response.status_code, "body": response.text[:2000]}

    def get(self, path: str, **params: Any) -> Any:
        return self.request("GET", path, params=params)

    def post(self, path: str, json: Any | None = None, **params: Any) -> Any:
        return self.request("POST", path, params=params, json=json)

    def put(self, path: str, json: Any | None = None, **params: Any) -> Any:
        return self.request("PUT", path, params=params, json=json)


def _clean(params: dict[str, Any] | None) -> dict[str, Any] | None:
    if not params:
        return None
    return {k: v for k, v in params.items() if v is not None and v != ""}
