SYNONYMS = {
    "buyer": ["customer", "user"],
    "buyers": ["customers", "users"],
    "customer": ["buyer", "user"],
    "customers": ["buyers", "users"],

    "purchase": ["order", "buy"],
    "purchases": ["orders", "buys"],
    "buy": ["purchase", "order"],
    "bought": ["purchase", "order"],

    "revenue": ["sales", "amount"],
    "sales": ["revenue", "amount"],

    "product": ["item"],
    "products": ["items"],
    "purchaser": ["buyer", "customer", "user"],
    "purchasers": ["buyers", "customers", "users"]
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