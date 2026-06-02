TABLE_FIXES = {
    "customer": "users",
    "customers": "users",
    "buyer": "users",
    "buyers": "users"
}

COLUMN_FIXES = {
    "users.full_name": "users.name",
    "products.title": "products.name"
}


def repair_sql(sql, validation):

    repaired_sql = sql

    for error in validation["errors"]:

        # Unknown table
        if "Unknown table:" in error:

            bad_table = (
                error.split(":")[1]
                .strip()
            )

            if bad_table in TABLE_FIXES:

                repaired_sql = repaired_sql.replace(
                    bad_table,
                    TABLE_FIXES[bad_table]
                )

        # Unknown column
        elif "Unknown column:" in error:

            bad_column = (
                error.split(":")[1]
                .strip()
            )

            if bad_column in COLUMN_FIXES:

                repaired_sql = repaired_sql.replace(
                    bad_column,
                    COLUMN_FIXES[bad_column]
                )

    return repaired_sql