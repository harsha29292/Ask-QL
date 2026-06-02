EVAL_SET = [

    # retrieval

    {
        "query": "top products bought by users",
        "expected_tables": [
            "products",
            "orders",
            "users"
        ]
    },

    {
        "query": "customers who bought electronics",
        "expected_tables": [
            "users",
            "orders",
            "categories"
        ]
    },

    {
        "query": "books purchases",
        "expected_tables": [
            "products",
            "categories"
        ]
    },

    {
        "query": "users with orders",
        "expected_tables": [
            "users",
            "orders"
        ]
    },

    {
        "query": "products bought by customers",
        "expected_tables": [
            "products",
            "users",
            "orders"
        ]
    },

    # aggregations

    {
        "query": "average order value",
        "expected_tables": [
            "orders"
        ]
    },

    {
        "query": "count customers",
        "expected_tables": [
            "users"
        ]
    },

    {
        "query": "total sales",
        "expected_tables": [
            "orders"
        ]
    },

    {
        "query": "number of orders",
        "expected_tables": [
            "orders"
        ]
    },

    # ranking

    {
        "query": "top selling products",
        "expected_tables": [
            "products",
            "order_items"
        ]
    },

    {
        "query": "lowest selling categories",
        "expected_tables": [
            "categories",
            "products"
        ]
    },

    {
        "query": "best selling products",
        "expected_tables": [
            "products",
            "order_items"
        ]
    },

    # filters

    {
        "query": "electronics purchases",
        "expected_tables": [
            "categories",
            "products"
        ]
    },

    {
        "query": "orders above 500",
        "expected_tables": [
            "orders"
        ]
    },

    {
        "query": "orders below 1000",
        "expected_tables": [
            "orders"
        ]
    },

    {
        "query": "electronics orders above 500",
        "expected_tables": [
            "orders",
            "categories"
        ]
    }
]