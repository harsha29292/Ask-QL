import psycopg2

# =========================
# DB CONNECTION
# =========================
def get_connection():
    conn = psycopg2.connect(
        dbname="askql",
        user="postgres",
        password="harsha123",
        host="127.0.0.1",
        port="5432"
    )
    conn.autocommit = True

    cursor = conn.cursor()
    cursor.execute("SET search_path TO public;")
    cursor.close()

    return conn


# =========================
# TABLES
# =========================
def get_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT relname
        FROM pg_class
        WHERE relkind = 'r'
        AND relnamespace = 'public'::regnamespace;
    """)

    tables = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return tables



def get_columns(conn, table_name):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = %s
        AND table_schema = 'public'
    """, (table_name,))

    columns = [{"name": row[0], "type": row[1]} for row in cursor.fetchall()]
    cursor.close()
    return columns



def get_primary_keys(conn, table_name):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT kcu.column_name
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
        WHERE tc.table_name = %s
        AND tc.table_schema = 'public'
        AND tc.constraint_type = 'PRIMARY KEY'
    """, (table_name,))

    kpk = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return kpk



def get_foreign_keys(conn, table_name):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            kcu.column_name,
            ccu.table_name,
            ccu.column_name
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
            ON tc.constraint_name = kcu.constraint_name
        JOIN information_schema.constraint_column_usage ccu
            ON ccu.constraint_name = tc.constraint_name
        WHERE tc.table_name = %s
        AND tc.table_schema = 'public'
        AND tc.constraint_type = 'FOREIGN KEY'
    """, (table_name,))

    fks = [
        {
            "column": row[0],
            "references": {
                "table": row[1],
                "column": row[2]
            }
        }
        for row in cursor.fetchall()
    ]

    cursor.close()
    return fks



def extract_schema():
    conn = get_connection()

    schema = {"tables": []}
    tables = get_tables(conn)

    for table in tables:
        schema["tables"].append({
            "name": table,
            "columns": get_columns(conn, table),
            "primary_key": get_primary_keys(conn, table),
            "foreign_keys": get_foreign_keys(conn, table)
        })

    conn.close()
    return schema