import os

print("Starting University Management System...")

os.system(
    "python -m uvicorn backend.main:app --reload"
)