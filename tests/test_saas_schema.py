from app.db.introspect import extract_schema

schema = extract_schema()

tables = schema["tables"]

print("TABLE COUNT:", len(tables))

for table in tables:
    print(table["name"])