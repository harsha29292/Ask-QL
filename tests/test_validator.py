from app.db.introspect import extract_schema
from app.core.sql_validator import (
    validate_sql
)

schema = extract_schema()

sqls = [

    """
    SELECT users.name
    FROM users
    """,

    """
    SELECT users.full_name
    FROM users
    """,

    """
    SELECT users.name
    FROM customer
    """
]

for sql in sqls:

    print("\n" + "=" * 60)

    print(
        validate_sql(
            sql,
            schema
        )
    )

