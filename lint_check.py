import subprocess, json
from collections import defaultdict
import os

try:
    res = subprocess.run(['uv', 'run', 'ruff', 'check', 'src/', 'tests/', '--output-format', 'json'], capture_output=True, text=True)
    out = json.loads(res.stdout)
    errors = defaultdict(list)
    for e in out:
        errors[e['filename']].append(f"Line {e['location']['row']}: {e['code']} - {e['message']}")
    
    with open('lint_errors.txt', 'w', encoding='utf-8') as f:
        for fname, errs in errors.items():
            f.write(f"--- {os.path.relpath(fname)} ---\n")
            for err in errs:
                f.write(f"{err}\n")
    print("Lint errors written to lint_errors.txt")
except Exception as e:
    print('Failed:', e)
