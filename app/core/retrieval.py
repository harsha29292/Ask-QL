def extract_relevant_tables(query, graph):
    query = query.lower()
    matched = []

    for table in graph:
        if table in query:
            matched.append(table)

    return matched