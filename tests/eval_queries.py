EVAL_SET = [

    {
        "query": "top products bought by users",
        "expected_tables": [
            "products",
            "orders",
            "users"
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
        "query": "average order value",
        "expected_tables": [
            "orders"
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
    }
]