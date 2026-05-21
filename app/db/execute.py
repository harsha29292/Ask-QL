import psycopg2

from app.db.introspect import get_connection


def execute_sql(sql):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        cursor.execute(sql)

        rows = cursor.fetchall()

        columns = [
            desc[0]
            for desc in cursor.description
        ]

        results = []

        for row in rows:
            results.append(
                dict(zip(columns, row))
            )

        return {
            "success": True,
            "rows": results
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:
        cursor.close()
        conn.close()