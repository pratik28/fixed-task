import json
import re
from collections import Counter

paths = Counter()
 ips = set() 
 total = 0
 
 log_path = "/environment/access.log"
out_path = "/environment/report.json"
http_method_re = re.compile(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ')

with open(log_path, "r", encoding="utf-8", errors="replace") as f:
    
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = http_method_re.search(line)
        if m:
            paths[m.group(1)] += 1

top_path = paths.most_common(1)[0][0] if paths else ""

with open(out_path, "w", encoding="utf-8") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "top_path": top_path 
        },
        out,
    )
print(f"wrote out_path")
