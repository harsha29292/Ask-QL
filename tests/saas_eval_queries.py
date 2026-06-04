SAAS_EVAL = [
    {
        "query": "top paying customers",
        "expected_tables": ["customers", "payments", "invoices"]
    },
    {
        "query": "highest revenue customers",
        "expected_tables": ["customers", "payments"]
    },
    {
        "query": "customers with active subscriptions",
        "expected_tables": ["customers", "subscriptions"]
    },
    {
        "query": "organizations with most users",
        "expected_tables": ["organizations", "users"]
    },
    {
        "query": "customers with overdue invoices",
        "expected_tables": ["customers", "invoices"]
    },
    {
        "query": "average invoice value",
        "expected_tables": ["invoices"]
    },
    {
        "query": "top subscription plans",
        "expected_tables": ["plans", "subscriptions"]
    },
    {
        "query": "users with most tickets",
        "expected_tables": ["users", "tickets"]
    },
    {
        "query": "organizations with highest revenue",
        "expected_tables": ["organizations", "customers", "payments"]
    },
    {
        "query": "customers with most invoices",
        "expected_tables": ["customers", "invoices"]
    }
]