# Enterprise Commerce MCPs

Public open-source project owned by **Pawan Gunjkar** (`pawangunjkar@gmail.com` · [GitHub](https://github.com/Pawangunjkar)). MIT licensed. See `OWNER.md` and `LICENSE`.

Standalone **Python MCP** project. It is **not** part of `enterprise-commerce-suite`. Each Spring Boot service and each React portal has its own FastMCP server that calls that application's HTTP API.

## Install

```bash
cd enterprise-commerce-mcps
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Run one server (stdio)

```bash
ecs-mcp-product-service
ecs-mcp-gst-tax-engine
ecs-mcp-ecommerce-storefront-portal
```

Override the target URL if you go through the gateway:

```bash
set ECS_GATEWAY_URL=http://localhost:8080
set ECS_SERVICE_URL=http://localhost:8080
ecs-mcp-product-service
```

Optional: `ECS_BEARER_TOKEN`, `ECS_TENANT_ID`.

## Cursor MCP config

Copy entries from `cursor-mcp.example.json` into Cursor MCP settings. Start with the six portal servers plus GST, product, cart, and payment; add more as needed. All 54 names are listed in `mcp-servers.txt`.

## Layout

- `src/ecs_mcp_core/` — shared HTTP client
- `src/ecs_mcps/` — one module per application
- `tools/generate_mcps.py` — regenerates the per-app servers from the API map

## Owner

- Name: Pawan Gunjkar
- Email: pawangunjkar@gmail.com
- GitHub: https://github.com/Pawangunjkar
- Visibility: public open source (MIT)
