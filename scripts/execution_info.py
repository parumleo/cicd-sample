from datetime import datetime, timezone
import os

# Get the current date and time in UTC
now = datetime.now(timezone.utc)

# Get the GitHub Actions Run ID from the environment
run_id = os.getenv("GITHUB_RUN_ID", "Not running in GitHub Actions")

print("===================================")
print("    Workflow Execution Details")
print("===================================")
print(f"Execution Date (UTC): {now.strftime('%Y-%m-%d')}")
print(f"Execution Time (UTC): {now.strftime('%H:%M:%S')}")
print(f"GitHub Actions Run ID: {run_id}")
print("===================================")
