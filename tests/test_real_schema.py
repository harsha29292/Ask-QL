from app.db.introspect import extract_schema
from pprint import pprint

schema = extract_schema()

print("TYPE:", type(schema))
print("TABLE COUNT:", len(schema))

first_table = list(schema.keys())[0]

print("\nFIRST TABLE:")
print(first_table)

print("\nFIRST TABLE DATA:")
pprint(schema[first_table])