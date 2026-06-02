from app.core.sql_repair import (
    repair_sql
)

sql = """
SELECT users.full_name
FROM users
"""

validation = {
    "valid": False,
    "errors": [
        "Unknown column: users.full_name"
    ]
}

repaired = repair_sql(
    sql,
    validation
)

print("ORIGINAL:")
print(sql)

print("\nREPAIRED:")
print(repaired)