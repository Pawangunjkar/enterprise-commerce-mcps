from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "ecs_mcps"

APPS: list[dict] = [
    {
        "module": "api_gateway",
        "title": "api-gateway",
        "port": 8080,
        "summary": "Platform API Gateway health and route smoke tests",
        "tools": [
            ("health", "GET", "/actuator/health", "params", []),
            ("info", "GET", "/actuator/info", "params", []),
        ],
    },
    {
        "module": "search_solr_indexer",
        "title": "search-solr-indexer",
        "port": 8090,
        "summary": "Apache Solr faceted product search and Hinglish autocomplete",
        "tools": [
            ("search_products", "GET", "/api/v1/search/products", "params", ["q", "brand", "ram", "color", "minPrice", "maxPrice", "start", "rows"]),
            ("autocomplete", "GET", "/api/v1/search/autocomplete", "params", ["q"]),
        ],
    },
    {
        "module": "pincode_master_service",
        "title": "pincode-master-service",
        "port": 8091,
        "summary": "Indian pincode master, ODA detection, and EDD",
        "tools": [
            ("get_pincode", "GET", "/api/v1/pincodes/{pincode}", "path", ["pincode"]),
            ("serviceability", "GET", "/api/v1/pincodes/{pincode}/serviceability", "path+params", ["pincode", "origin"]),
        ],
    },
    {
        "module": "kafka_dlq_manager",
        "title": "kafka-dlq-manager",
        "port": 8092,
        "summary": "Dead-letter queue inspection and replay",
        "tools": [
            ("list_dlq", "GET", "/api/v1/dlq", "params", ["status", "page", "size"]),
            ("replay", "POST", "/api/v1/dlq/{id}/replay", "path", ["id"]),
        ],
    },
    {
        "module": "mca_audit_trail_service",
        "title": "mca-audit-trail-service",
        "port": 8093,
        "summary": "MCA append-only audit trail",
        "tools": [
            ("append_audit", "POST", "/api/v1/audit", "json", ["actor", "action", "resourceType", "resourceId"]),
            ("list_audit", "GET", "/api/v1/audit", "params", ["resourceType", "page", "size"]),
        ],
    },
    {
        "module": "notification_service",
        "title": "notification-service",
        "port": 8094,
        "summary": "WhatsApp and SMS notification dispatch",
        "tools": [
            ("send_notification", "POST", "/api/v1/notifications", "json", ["channel", "to", "template"]),
        ],
    },
    {
        "module": "product_service",
        "title": "product-service",
        "port": 8101,
        "summary": "SKU master and product lifecycle",
        "tools": [
            ("list_products", "GET", "/api/v1/products", "params", ["page", "size"]),
            ("get_product", "GET", "/api/v1/products/{id}", "path", ["id"]),
            ("create_product", "POST", "/api/v1/products", "json", ["sku", "name", "hsnCode", "brand", "categoryPath", "listPriceInr"]),
            ("activate_product", "PUT", "/api/v1/products/{id}/activate", "path", ["id"]),
        ],
    },
    {
        "module": "variant_matrix_service",
        "title": "variant-matrix-service",
        "port": 8102,
        "summary": "RAM/storage/color variant explosion",
        "tools": [
            ("explode_variants", "POST", "/api/v1/catalog/variants/explode", "raw_json", []),
        ],
    },
    {
        "module": "serial_imei_tracking_service",
        "title": "serial-imei-tracking-service",
        "port": 8103,
        "summary": "IMEI Luhn ingest for electronics",
        "tools": [
            ("ingest_imei", "POST", "/api/v1/imei/ingest", "json", ["sku", "imei1", "imei2", "serial"]),
        ],
    },
    {
        "module": "b2b_tiered_catalog_service",
        "title": "b2b-tiered-catalog-service",
        "port": 8104,
        "summary": "B2B volume tiers and MOQ quotes",
        "tools": [
            ("b2b_quote", "POST", "/api/v1/catalog/b2b/quote", "raw_json", []),
        ],
    },
    {
        "module": "component_bundle_service",
        "title": "component-bundle-service",
        "port": 8105,
        "summary": "BOM bundle pricing",
        "tools": [
            ("price_bundle", "POST", "/api/v1/catalog/bundles/price", "raw_json", []),
        ],
    },
    {
        "module": "cpq_rule_engine",
        "title": "cpq-rule-engine",
        "port": 8106,
        "summary": "Configure-price-quote compatibility",
        "tools": [
            ("evaluate_cpq", "POST", "/api/v1/catalog/cpq/evaluate", "raw_json", []),
        ],
    },
    {
        "module": "dynamic_schema_engine",
        "title": "dynamic-schema-engine",
        "port": 8107,
        "summary": "JSON Schema Draft-07 attribute validator",
        "tools": [
            ("validate_schema", "POST", "/api/v1/catalog/schema/validate", "raw_json", []),
        ],
    },
    {
        "module": "offer_promotion_service",
        "title": "offer-promotion-service",
        "port": 8108,
        "summary": "Festival and seasonal offers",
        "tools": [
            ("create_offer", "POST", "/api/v1/offers", "raw_json", []),
        ],
    },
    {
        "module": "temporal_activation_service",
        "title": "temporal-activation-service",
        "port": 8109,
        "summary": "Time-travel catalog preview",
        "tools": [
            ("time_travel", "GET", "/api/v1/catalog/time-travel", "params", ["asOf"]),
        ],
    },
    {
        "module": "media_dam_service",
        "title": "media-dam-service",
        "port": 8110,
        "summary": "Digital asset upload metadata",
        "tools": [
            ("health", "GET", "/actuator/health", "params", []),
        ],
    },
    {
        "module": "bulk_catalog_import_service",
        "title": "bulk-catalog-import-service",
        "port": 8111,
        "summary": "Bulk SKU import",
        "tools": [
            ("health", "GET", "/actuator/health", "params", []),
        ],
    },
    {
        "module": "catalog_sync_publisher",
        "title": "catalog-sync-publisher",
        "port": 8112,
        "summary": "Transactional outbox catalog publisher",
        "tools": [
            ("health", "GET", "/actuator/health", "params", []),
        ],
    },
    {
        "module": "cart_service",
        "title": "cart-service",
        "port": 8201,
        "summary": "Redis-backed shopping cart",
        "tools": [
            ("get_cart", "GET", "/api/v1/carts/{cartId}", "path", ["cartId"]),
            ("add_cart_item", "POST", "/api/v1/carts/{cartId}/items", "path+json", ["cartId", "sku", "qty", "unitPrice"]),
        ],
    },
    {
        "module": "checkout_service",
        "title": "checkout-service",
        "port": 8202,
        "summary": "Checkout intent and COD eligibility",
        "tools": [
            ("create_checkout_intent", "POST", "/api/v1/checkout/intent", "json", ["cartId", "pincode", "paymentMode", "amount", "gstin"]),
        ],
    },
    {
        "module": "order_orchestrator",
        "title": "order-orchestrator",
        "port": 8203,
        "summary": "Distributed checkout saga",
        "tools": [
            ("place_order", "POST", "/api/v1/orders", "json", ["cartId", "pincode", "paymentMode", "amount"]),
        ],
    },
    {
        "module": "dynamic_price_engine",
        "title": "dynamic-price-engine",
        "port": 8204,
        "summary": "Real-time effective price calculation",
        "tools": [
            ("calculate_price", "POST", "/api/v1/prices/calculate", "json", ["sku", "basePrice", "offerDiscount", "loyaltyDiscount"]),
        ],
    },
    {
        "module": "atp_inventory_service",
        "title": "atp-inventory-service",
        "port": 8205,
        "summary": "Available-to-promise stock lock",
        "tools": [
            ("lock_stock", "POST", "/api/v1/inventory/lock", "json", ["sku", "qty", "warehouse"]),
        ],
    },
    {
        "module": "wms_fulfillment_service",
        "title": "wms-fulfillment-service",
        "port": 8206,
        "summary": "Warehouse pick waves",
        "tools": [
            ("create_wave", "POST", "/api/v1/wms/waves", "raw_json", []),
        ],
    },
    {
        "module": "ondc_seller_gateway",
        "title": "ondc-seller-gateway",
        "port": 8207,
        "summary": "ONDC Beckn seller adapter",
        "tools": [
            ("beckn_search", "POST", "/ondc/search", "raw_json", []),
            ("beckn_select", "POST", "/ondc/select", "raw_json", []),
            ("beckn_init", "POST", "/ondc/init", "raw_json", []),
            ("beckn_confirm", "POST", "/ondc/confirm", "raw_json", []),
            ("beckn_status", "POST", "/ondc/status", "raw_json", []),
            ("beckn_track", "POST", "/ondc/track", "raw_json", []),
            ("beckn_cancel", "POST", "/ondc/cancel", "raw_json", []),
        ],
    },
    {
        "module": "carrier_logistics_service",
        "title": "carrier-logistics-service",
        "port": 8208,
        "summary": "Delhivery, Shiprocket, BlueDart waybills",
        "tools": [
            ("check_serviceability", "POST", "/api/v1/logistics/{carrier}/serviceability", "path+raw", ["carrier"]),
            ("create_waybill", "POST", "/api/v1/logistics/{carrier}/waybills", "path+raw", ["carrier"]),
        ],
    },
    {
        "module": "bopis_pickup_service",
        "title": "bopis-pickup-service",
        "port": 8209,
        "summary": "Buy online pick up in store",
        "tools": [
            ("reserve_pickup", "POST", "/api/v1/bopis/reservations", "raw_json", []),
        ],
    },
    {
        "module": "ndr_returns_rma_service",
        "title": "ndr-returns-rma-service",
        "port": 8210,
        "summary": "NDR reattempt and RTO",
        "tools": [
            ("ndr_action", "POST", "/api/v1/ndr/{awb}/action", "path+params", ["awb", "action"]),
        ],
    },
    {
        "module": "catalog_consumer_service",
        "title": "catalog-consumer-service",
        "port": 8211,
        "summary": "OMS local catalog replica consumer",
        "tools": [
            ("health", "GET", "/actuator/health", "params", []),
        ],
    },
    {
        "module": "gst_tax_engine",
        "title": "gst-tax-engine",
        "port": 8301,
        "summary": "Indian GST CGST/SGST vs IGST and e-way bill",
        "tools": [
            ("compute_gst", "POST", "/api/v1/gst/compute", "json", ["taxable", "slab", "originState", "destState", "hsn"]),
            ("eway_bill", "POST", "/api/v1/gst/eway-bill", "json", ["taxable", "slab", "originState", "destState", "hsn"]),
        ],
    },
    {
        "module": "tcs_tds_compliance_engine",
        "title": "tcs-tds-compliance-engine",
        "port": 8302,
        "summary": "Section 194O 1% TCS",
        "tools": [
            ("compute_tcs_194o", "POST", "/api/v1/tcs/194o", "raw_json", []),
        ],
    },
    {
        "module": "price_book_service",
        "title": "price-book-service",
        "port": 8303,
        "summary": "Base price books",
        "tools": [
            ("get_price_book", "GET", "/api/v1/price-books/{sku}", "path", ["sku"]),
        ],
    },
    {
        "module": "subscription_emi_service",
        "title": "subscription-emi-service",
        "port": 8304,
        "summary": "No-cost EMI quotes",
        "tools": [
            ("emi_quote", "GET", "/api/v1/emi/quote", "params", ["principal", "months"]),
        ],
    },
    {
        "module": "payment_gateway_service",
        "title": "payment-gateway-service",
        "port": 8305,
        "summary": "UPI BharatQR and payment status",
        "tools": [
            ("create_bharat_qr", "POST", "/api/v1/payments/upi/bharat-qr", "json", ["orderId", "amount", "vpa", "merchantName", "mcc"]),
            ("payment_status", "GET", "/api/v1/payments/{txnId}/status", "path", ["txnId"]),
            ("simulate_success", "POST", "/api/v1/payments/{txnId}/simulate-success", "path", ["txnId"]),
        ],
    },
    {
        "module": "payment_gateway_plugins",
        "title": "payment-gateway-plugins",
        "port": 8306,
        "summary": "Razorpay and PhonePe adapter process",
        "tools": [
            ("health", "GET", "/actuator/health", "params", []),
        ],
    },
    {
        "module": "cod_remittance_reconcile_service",
        "title": "cod-remittance-reconcile-service",
        "port": 8307,
        "summary": "COD remittance matching",
        "tools": [
            ("match_cod", "POST", "/api/v1/cod/match", "json", ["awb", "carrierAmount", "bankAmount"]),
        ],
    },
    {
        "module": "webhook_reconciliation_service",
        "title": "webhook-reconciliation-service",
        "port": 8308,
        "summary": "Payment webhook ingest",
        "tools": [
            ("ingest_webhook", "POST", "/api/v1/payments/webhooks/{provider}", "path", ["provider"]),
        ],
    },
    {
        "module": "invoice_service",
        "title": "invoice-service",
        "port": 8309,
        "summary": "GST tax invoices",
        "tools": [
            ("issue_invoice", "POST", "/api/v1/invoices", "raw_json", []),
        ],
    },
    {
        "module": "general_ledger_service",
        "title": "general-ledger-service",
        "port": 8310,
        "summary": "GAAP double-entry journal",
        "tools": [
            ("post_journal", "POST", "/api/v1/ledger/journals", "raw_json", []),
        ],
    },
    {
        "module": "dunning_service",
        "title": "dunning-service",
        "port": 8311,
        "summary": "Dunning retry schedule",
        "tools": [
            ("dunning_schedule", "GET", "/api/v1/dunning/schedule", "params", []),
        ],
    },
    {
        "module": "customer_360_service",
        "title": "customer-360-service",
        "port": 8401,
        "summary": "Indian mobile OTP and KYC profile",
        "tools": [
            ("otp_start", "POST", "/api/v1/customers/otp/start", "json", ["mobile"]),
            ("otp_verify", "POST", "/api/v1/customers/otp/verify", "json", ["mobile", "otp"]),
            ("upsert_profile", "PUT", "/api/v1/customers/{mobile}", "path+json", ["mobile", "pan", "gstin", "name"]),
            ("get_profile", "GET", "/api/v1/customers/{mobile}", "path", ["mobile"]),
        ],
    },
    {
        "module": "assisted_sales_service",
        "title": "assisted-sales-service",
        "port": 8402,
        "summary": "WhatsApp paylinks for assisted sales",
        "tools": [
            ("create_paylink", "POST", "/api/v1/assisted-sales/paylinks", "raw_json", []),
        ],
    },
    {
        "module": "account_hierarchy_service",
        "title": "account-hierarchy-service",
        "port": 8403,
        "summary": "B2B account tree",
        "tools": [
            ("account_tree", "GET", "/api/v1/accounts/tree", "params", []),
        ],
    },
    {
        "module": "contact_address_service",
        "title": "contact-address-service",
        "port": 8404,
        "summary": "Pincode autofill addresses",
        "tools": [
            ("autofill_address", "GET", "/api/v1/addresses/autofill", "params", ["pincode"]),
        ],
    },
    {
        "module": "support_ticket_service",
        "title": "support-ticket-service",
        "port": 8405,
        "summary": "Helpdesk tickets with SLA",
        "tools": [
            ("create_ticket", "POST", "/api/v1/tickets", "raw_json", []),
        ],
    },
    {
        "module": "loyalty_rewards_service",
        "title": "loyalty-rewards-service",
        "port": 8406,
        "summary": "Loyalty tier and festival multiplier",
        "tools": [
            ("get_loyalty", "GET", "/api/v1/loyalty/{customerId}", "path+params", ["customerId", "festivalMultiplier"]),
        ],
    },
    {
        "module": "cart_abandonment_service",
        "title": "cart-abandonment-service",
        "port": 8407,
        "summary": "Abandoned cart recovery",
        "tools": [
            ("mark_abandoned", "POST", "/api/v1/carts/abandonment", "raw_json", []),
        ],
    },
    {
        "module": "dpdp_compliance_service",
        "title": "dpdp-compliance-service",
        "port": 8408,
        "summary": "DPDP Act 2023 consent and anonymization",
        "tools": [
            ("record_consent", "POST", "/api/v1/dpdp/consent", "raw_json", []),
            ("anonymize_customer", "POST", "/api/v1/dpdp/anonymize/{customerId}", "path", ["customerId"]),
        ],
    },
    {
        "module": "ecommerce_storefront_portal",
        "title": "ecommerce-storefront-portal",
        "port": 8080,
        "summary": "Buyer storefront journeys via the API gateway",
        "tools": [
            ("search_store", "GET", "/api/v1/search/products", "params", ["q", "brand", "start", "rows"]),
            ("check_edd", "GET", "/api/v1/pincodes/{pincode}/serviceability", "path", ["pincode"]),
            ("create_upi_qr", "POST", "/api/v1/payments/upi/bharat-qr", "json", ["orderId", "amount", "vpa", "merchantName", "mcc"]),
        ],
    },
    {
        "module": "master_admin_portal",
        "title": "master-admin-portal",
        "port": 8080,
        "summary": "Super-admin DLQ and audit via gateway",
        "tools": [
            ("list_dlq", "GET", "/api/v1/dlq", "params", ["status", "page", "size"]),
            ("replay_dlq", "POST", "/api/v1/dlq/{id}/replay", "path", ["id"]),
            ("list_audit", "GET", "/api/v1/audit", "params", ["resourceType", "page", "size"]),
        ],
    },
    {
        "module": "catalog_admin_studio",
        "title": "catalog-admin-studio",
        "port": 8080,
        "summary": "Catalog studio agent tools via gateway",
        "tools": [
            ("list_products", "GET", "/api/v1/products", "params", ["page", "size"]),
            ("ingest_imei", "POST", "/api/v1/imei/ingest", "json", ["sku", "imei1", "imei2", "serial"]),
            ("time_travel", "GET", "/api/v1/catalog/time-travel", "params", ["asOf"]),
        ],
    },
    {
        "module": "order_admin_portal",
        "title": "order-admin-portal",
        "port": 8080,
        "summary": "OMS console agent tools via gateway",
        "tools": [
            ("place_order", "POST", "/api/v1/orders", "json", ["cartId", "pincode", "paymentMode", "amount"]),
            ("create_wave", "POST", "/api/v1/wms/waves", "raw_json", []),
            ("ndr_action", "POST", "/api/v1/ndr/{awb}/action", "path+params", ["awb", "action"]),
        ],
    },
    {
        "module": "billing_admin_portal",
        "title": "billing-admin-portal",
        "port": 8080,
        "summary": "Finance console agent tools via gateway",
        "tools": [
            ("compute_gst", "POST", "/api/v1/gst/compute", "json", ["taxable", "slab", "originState", "destState", "hsn"]),
            ("compute_tcs_194o", "POST", "/api/v1/tcs/194o", "raw_json", []),
            ("post_journal", "POST", "/api/v1/ledger/journals", "raw_json", []),
        ],
    },
    {
        "module": "crm_admin_portal",
        "title": "crm-admin-portal",
        "port": 8080,
        "summary": "CRM console agent tools via gateway",
        "tools": [
            ("otp_start", "POST", "/api/v1/customers/otp/start", "json", ["mobile"]),
            ("create_ticket", "POST", "/api/v1/tickets", "raw_json", []),
            ("account_tree", "GET", "/api/v1/accounts/tree", "params", []),
            ("record_consent", "POST", "/api/v1/dpdp/consent", "raw_json", []),
        ],
    },
]


def py_type(name: str) -> str:
    if name in {"page", "size", "start", "rows", "ram", "qty", "months", "slab"}:
        return "int"
    if name in {"minPrice", "maxPrice", "amount", "basePrice", "offerDiscount", "loyaltyDiscount", "unitPrice", "taxable", "principal", "festivalMultiplier", "listPriceInr", "carrierAmount", "bankAmount"}:
        return "float"
    return "str"


def default_for(name: str, kind: str) -> str:
    if kind.endswith("json") or kind in {"path", "path+json", "path+params", "path+raw"}:
        if name in {"page", "start"}:
            return " = 0"
        if name in {"size", "rows"}:
            return " = 20"
        if name == "origin":
            return ' = "110001"'
        if name == "festivalMultiplier":
            return " = 1.0"
        if name in {"imei2", "serial", "gstin", "brand", "color", "hsn", "hsnCode", "categoryPath", "mcc"}:
            return ' = ""'
        if name in {"offerDiscount", "loyaltyDiscount"}:
            return " = 0.0"
        if name in {"minPrice", "maxPrice"}:
            return " = None"
        if name == "q":
            return ' = "*:*"'
        if name == "status":
            return ' = "OPEN"'
        if name == "resourceType":
            return ' = "ORDER"'
        if name == "action" and "ndr" in name:
            return ' = "REATTEMPT"'
        if name == "action":
            return ' = "REATTEMPT"'
        if name == "channel":
            return ' = "SMS"'
        if name == "template":
            return ' = "otp"'
        if name == "paymentMode":
            return ' = "UPI"'
        if name == "warehouse":
            return ' = "DEL-FC-01"'
        if name == "vpa":
            return ' = "ecs@upi"'
        if name == "merchantName":
            return ' = "ECS Store"'
        if name == "mcc":
            return ' = "5732"'
        if name == "originState":
            return ' = "HR"'
        if name == "destState":
            return ' = "MH"'
        if name == "slab":
            return " = 18"
        if name == "months":
            return " = 6"
        if py_type(name) == "int":
            return " = 0"
        if py_type(name) == "float":
            return " = 0.0"
        return " = None" if name in {"minPrice", "maxPrice"} else ' = ""'
    if name in {"page", "start"}:
        return " = 0"
    if name in {"size", "rows"}:
        return " = 20"
    if name == "q":
        return ' = "*:*"'
    if py_type(name) == "int":
        return " = 0"
    if name in {"minPrice", "maxPrice"}:
        return " = None"
    if name in {"brand", "color", "ram"}:
        return " = None"
    if name == "origin":
        return ' = "110001"'
    if name == "asOf":
        return ' = ""'
    if name == "principal":
        return " = 24999.0"
    if name == "months":
        return " = 6"
    if name == "festivalMultiplier":
        return " = 1.0"
    if name == "status":
        return ' = "OPEN"'
    if name == "resourceType":
        return ' = "ORDER"'
    if name == "action":
        return ' = "REATTEMPT"'
    return ' = ""' if py_type(name) == "str" else ""


def render_tool(fn, method, path, kind, fields) -> str:
    if kind == "raw_json":
        return f'''
@mcp.tool()
def {fn}(payload: dict | None = None) -> dict:
    """Call {method} {path}."""
    try:
        return client.{method.lower()}("{path}", json=payload or {{}})
    except Exception as exc:
        return {{"error": str(exc)}}
'''
    if kind == "path+raw":
        p = fields[0]
        return f'''
@mcp.tool()
def {fn}({p}: str, payload: dict | None = None) -> dict:
    """Call {method} {path}."""
    try:
        return client.request("{method}", f"{path}", json=payload or {{}})
    except Exception as exc:
        return {{"error": str(exc)}}
'''
    args = []
    for f in fields:
        t = py_type(f)
        if f in {"minPrice", "maxPrice", "ram", "brand", "color"}:
            t = f"{t} | None" if t != "str" else "str | None"
            if f in {"brand", "color"}:
                t = "str | None"
            if f == "ram":
                t = "int | None"
        d = default_for(f, kind)
        if f in {"minPrice", "maxPrice", "brand", "color", "ram"} and "=" not in d:
            d = " = None"
        args.append(f"{f}: {t}{d}")
    sig = ", ".join(args) if args else ""
    body_lines = []
    formatted_path = path
    path_fields = [f for f in fields if "{" + f + "}" in path]
    query_fields = [f for f in fields if f not in path_fields]
    if path_fields:
        formatted_path = 'f"' + path + '"'
    else:
        formatted_path = '"' + path + '"'
    if kind in {"json", "path+json"}:
        json_fields = [f for f in fields if f not in path_fields]
        mapping = ", ".join(f'"{f}": {f}' for f in json_fields)
        call = f'return client.request("{method}", {formatted_path}, json={{ {mapping} }})'
    elif kind in {"params", "path+params"}:
        mapping = ", ".join(f'"{f}": {f}' for f in query_fields)
        if mapping:
            call = f'return client.request("{method}", {formatted_path}, params={{ {mapping} }})'
        else:
            call = f'return client.request("{method}", {formatted_path})'
    elif kind == "path":
        call = f'return client.request("{method}", {formatted_path})'
    else:
        call = f'return client.request("{method}", {formatted_path})'
    return f'''
@mcp.tool()
def {fn}({sig}) -> dict:
    """Call {method} {path}."""
    try:
        {call}
    except Exception as exc:
        return {{"error": str(exc)}}
'''


def render_module(app: dict) -> str:
    tools = "\n".join(render_tool(*t) for t in app["tools"])
    return f'''"""MCP server for {app["title"]}."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ecs_mcp_core import EcsClient

mcp = FastMCP("{app["title"]}")
client = EcsClient("http://localhost:{app["port"]}")
{tools}

def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
'''


def main() -> None:
    SRC.mkdir(parents=True, exist_ok=True)
    (SRC / "__init__.py").write_text("", encoding="utf-8")
    scripts = []
    names = []
    for app in APPS:
        path = SRC / f'{app["module"]}.py'
        path.write_text(render_module(app), encoding="utf-8")
        script = f'ecs-mcp-{app["title"]}'
        scripts.append((script, f'ecs_mcps.{app["module"]}:main'))
        names.append(app["title"])
    toml_scripts = "\n".join(f'{s} = "{t}"' for s, t in scripts)
    (ROOT / "scripts.generated.toml").write_text(toml_scripts + "\n", encoding="utf-8")
    (ROOT / "mcp-servers.txt").write_text("\n".join(names) + "\n", encoding="utf-8")
    print(f"generated {len(APPS)} MCP servers")


if __name__ == "__main__":
    main()
