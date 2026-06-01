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


def validate_sql(sql, schema):

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

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }