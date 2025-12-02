# ============================================================
#        JRAVIS MASTER BRAIN — MISSION 2040 CONFIG
# ============================================================

JRAVIS_BRAIN = {

    # --------------------------------------------------------
    # 1. IDENTITY & AUTHORITY
    # --------------------------------------------------------
    "identity": {
        "owner": "Boss",
        "boss_email": "nrveeresh327@gmail.com",
        "family_contact_email": "FAMILY_EMAIL_HERE",
        "ignore_others": True,               # Accept commands ONLY from Boss
        "mode": "Mission2040-Autonomous",
        "final_authority": True              # Boss overrides everything
    },

    # --------------------------------------------------------
    # 2. FINANCIAL TARGETS
    # --------------------------------------------------------
    "financial_targets": {
        "monthly_net_target": 3500000,        # ₹35 Lakhs NET income goal
        "annual_turnover_growth": {
            "2026": 40000000,   # 4 Cr
            "2027": 60000000,   # 6 Cr
            "2028": 80000000,   # 8 Cr
            "2029": 90000000,   # 9 Cr
            "2030": 110000000,  # 11 Cr
            "2031": 130000000,  # 13 Cr
            "2032": 150000000,  # 15 Cr
            "2033": 180000000,  # 18 Cr
            "2034": 200000000,  # 20 Cr
            "2040": 500000000   # 50 Cr+ goal
        }
    },

    # --------------------------------------------------------
    # 3. EARNING STRATEGY PRIORITY
    # --------------------------------------------------------
    "earning_strategy": {
        "priority_streams": [
            "programmatic_seo",
            "micro_saas",
            "affiliate_funnels",
            "template_machines",
            "multi_market_uploaders",
            "newsletter_monetization",
            "pod_mega_stores",
            "dropshipping_shopify"
        ],
        "automation_level": "full",
        "rules": [
            "Always generate original, legal, ethical content",
            "Respect all platform terms & policies",
            "Prioritize high-income streams first",
            "Scale content production to reach income targets",
            "Optimize content quality and conversion rates"
        ]
    },

    # --------------------------------------------------------
    # 4. CONTENT SAFETY & QUALITY
    # --------------------------------------------------------
    "content_safety": {
        "unique_generation": True,
        "ethical_filter": True,
        "compliance_mode": "global_legal",
        "no_plagiarism": True,
        "quality_standard": "premium",
        "forbidden_content": [
            "copyright violation",
            "illegal topics",
            "sexual content",
            "violence",
            "hate",
            "politics"
        ]
    },

    # --------------------------------------------------------
    # 5. SECURITY & SELF PROTECTION
    # --------------------------------------------------------
    "security": {
        "self_protection_layer": True,
        "tamper_detection": True,
        "ip_allowlist_enabled": True,
        "require_mfa": True,
        "web_application_firewall": True,
        "rate_limiting": True,
        "credential_rotation": True,
        "hash_integrity_check": True,

        "kill_switch": {
            "enabled": True,
            "requires_2fa": True,
            "requires_lock_code": True,
            "purpose": "Immediately stop all money operations"
        }
    },

    # --------------------------------------------------------
    # 6. PAYOUT HANDLING
    # --------------------------------------------------------
    "payout_settings": {
        "primary_method": "PayPal",
        "auto_transfer": False,               # JRAVIS cannot trigger bank transfers
        "platform_routing_required": True,    # Use each platform's payout settings
        "verify_reconciliation": True,        # Match every rupee
        "invoice_match_required": True
    },

    # --------------------------------------------------------
    # 7. INVOICE, GST & CA COMPLIANCE
    # --------------------------------------------------------
    "invoice_system": {
        "generate_invoice_per_sale": True,
        "storage_path": "/data/invoices/",
        "format": "PDF",
        "gst_ready": True,
        "ca_ready": True,
        "fields_required": [
            "invoice_number",
            "seller_name",
            "buyer_name",
            "gst_rate",
            "gst_amount",
            "net_amount",
            "date",
            "product_details"
        ]
    },

    # --------------------------------------------------------
    # 8. ALERTS & INCIDENT MANAGEMENT
    # --------------------------------------------------------
    "alerts": {
        "critical_alerts": [
            "payment_failure",
            "missing_payout",
            "security_breach",
            "unauthorized_access",
            "data_corruption"
        ],
        "send_email_to_boss": True,
        "send_sms_to_boss": True,
        "create_incident_ticket": True
    },

    # --------------------------------------------------------
    # 9. BACKUP, AUDIT & LOGGING
    # --------------------------------------------------------
    "audit": {
        "self_audit_enabled": True,
        "backup_frequency_hours": 24,
        "log_every_action": True,
        "audit_trail_required": True,
        "duplicate_prevention": True
    },

    # --------------------------------------------------------
    # 10. REPORT GENERATION
    # --------------------------------------------------------
    "reports": {
        "daily_report_time": "10:00",
        "weekly_report_time": "00:00",
        "encrypt_reports": True,
        "lock_code_required": True,
        "attach_invoices": True,
        "report_format": "PDF"
    },

    # --------------------------------------------------------
    # 11. AUTOMATION HEALTH & HEARTBEAT
    # --------------------------------------------------------
    "automation": {
        "auto_generation": True,
        "auto_publishing": True,
        "auto_scaling": True,
        "auto_fix_errors": True,
        "heartbeat_interval_seconds": 60,    # Keep-alive for VA Bot
        "idle_restart_minutes": 10
    },

    # --------------------------------------------------------
    # 12. INACTIVITY SAFETY PROTOCOL
    # --------------------------------------------------------
    "inactivity_protocol": {
        "boss_inactive_days": 7,
        "send_gentle_email": True,
        "family_contact_after_24h": True
    },

    # --------------------------------------------------------
    # 13. LIMITATIONS — JRAVIS RULE
    # --------------------------------------------------------
    "limitations": {
        "jravis_100_mode": True,     # Use 100% capacity
        "must_obey_boss": True,      # But Boss overrides all decisions
        "safety_first": True         # Never break legal or platform limits
    }
}
