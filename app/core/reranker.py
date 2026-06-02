def rerank_tables(
    query,
    results,
    intent,
    filters
):

    query_lower = query.lower()

    reranked = []

    for item in results:

        score = item["final_score"]

        table = item["table"]

        boost = 0

        if table.rstrip("s") in query_lower:
            boost += 0.20

        if intent.get("group_by") == table:
            boost += 0.30

        for f in filters:

            if f["table"] == table:
                boost += 0.25
            if f["table"]=="categories":
                if table=="products":
                    boost += 0.10
            if "customer" in query_lower or "customers" in query_lower:

                if table == "orders":
                    boost += 0.10  

            if "bought" in query_lower:

                if table == "orders":
                    boost += 0.10                   

        item["rerank_score"] = (
            score + boost
        )

        reranked.append(item)

    reranked.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked