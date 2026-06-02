SYNONYMS={

    "paying": [
        "payments",
        "invoices",
        "revenue"
    ],

    "payment": [
        "payments",
        "invoice"
    ],

    "payments": [
        "invoice",
        "revenue"
    ],

    "revenue": [
        "payments",
        "invoices"
    ],

    "subscription": [
        "subscriptions",
        "plans"
    ],

    "subscriptions": [
        "plans"
    ],

    "invoice": [
        "invoices",
        "payments"
    ],

    "invoices": [
        "payments",
        "revenue"
    ]
}

def rewrite_query(query: str):
    tokens = query.lower().split()

    expanded = []

    for token in tokens:

        expanded.append(token)

        if token in SYNONYMS:
            expanded.extend(
                SYNONYMS[token]
            )

    return " ".join(expanded)