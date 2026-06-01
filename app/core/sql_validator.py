def build_schema_lookup(schema):

    lookup = {}

    for table in schema["tables"]:

        lookup[table["name"]] = {
            col["name"]
            for col in table["columns"]
        }

    return lookup

import re


def validate_tables(sql, schema_lookup):

    errors = []

    tables = re.findall(
        r"(?:FROM|JOIN)\s+(\w+)",
        sql,
        re.IGNORECASE
    )

    for table in tables:

        if table not in schema_lookup:

            errors.append(
                f"Unknown table: {table}"
            )

    return errors


def validate_columns(sql, schema_lookup):

    errors = []

    references = re.findall(
        r"(\w+)\.(\w+)",
        sql
    )

    for table, column in references:

        if table not in schema_lookup:
            continue

        if column not in schema_lookup[table]:

            errors.append(
                f"Unknown column: {table}.{column}"
            )

    return errors


def validate_sql(sql, schema,join_edges=None, graph=None):

    schema_lookup = build_schema_lookup(
        schema
    )

    errors = []

    
    errors.extend(
        validate_tables(
            sql,
            schema_lookup
        )
    )

    errors.extend(
        validate_columns(
            sql,
            schema_lookup
        )
    )
    if join_edges and graph:
        errors.extend(
            validate_join_edges(
                join_edges,
                graph
            )
        )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
def validate_join_edges(join_edges, graph):

    errors = []

    for source, target in join_edges:

        valid = False

        for rel in graph[source]["relations"]:

            if rel["to"] == target:
                valid = True
                break

        if not valid:

            errors.append(
                f"Invalid join: {source} -> {target}"
            )

    return errors    