import json
import sys
import os

path = sys.argv[1] if len(sys.argv) > 1 else "/environment/report.json"

if not os.path.exists(path):
    raise SystemExit(f"Missing artifact: {path}")

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

required = {"total_requests", "unique_ips", "top_path"}
missing = required - set(data.keys())
if missing:
    raise SystemExit(f"Missing keys in JSON: {sorted(missing)}")

print("verification ok")
