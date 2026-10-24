
from datetime import datetime, timezone
import os

now = datetime.now(timezone.utc)

run_id = os.getenv("GITHUB_RUN_ID", "Not available")
pr_number = os.getenv("PR_NUMBER", "Not available")
source_branch = os.getenv("SOURCE_BRANCH", "Not available")
target_branch = os.getenv("TARGET_BRANCH", "Not available")

print("===================================")
print("    Pull Request Execution Details")
print("===================================")
print(f"Pull Request Number: {pr_number}")
print(f"Source Branch: {source_branch}")
print(f"Target Branch: {target_branch}")
print(f"Execution Date (UTC): {now.strftime('%Y-%m-%d')}")
print(f"Execution Time (UTC): {now.strftime('%H:%M:%S')}")
print(f"GitHub Actions Run ID: {run_id}")
print("===================================")
