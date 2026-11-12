import sys
import os

# Add project root directory
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, project_root)

from config.database import engine

try:
    connection = engine.connect()

    print("SUCCESS : PostgreSQL Connected")

    connection.close()

except Exception as ex:

    print("FAILED")

    print(ex)