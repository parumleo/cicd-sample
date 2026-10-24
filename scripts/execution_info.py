from datetime import datetime, timezone
import os

# Read inputs passed by GitHub Actions
environment = os.getenv("TARGET_ENV", "dev")
message = os.getenv("CUSTOM_MESSAGE", "No message provided")

# Get current date and time in UTC
now = datetime.now(timezone.utc)

# Get GitHub Actions Run ID
run_id = os.getenv("GITHUB_RUN_ID", "Not running in GitHub Actions")

print("===================================")
print("    Workflow Execution Details")
print("===================================")
print(f"Environment: {environment}")
print(f"Custom Message: {message}")
print(f"Execution Date (UTC): {now.strftime('%Y-%m-%d')}")
print(f"Execution Time (UTC): {now.strftime('%H:%M:%S')}")
print(f"GitHub Actions Run ID: {run_id}")
print("===================================")
