from config.database import engine

try:

    conn = engine.connect()

    print(
        "SUCCESS: PostgreSQL Connected"
    )

    conn.close()

except Exception as e:

    print(
        f"ERROR: {e}"
    )