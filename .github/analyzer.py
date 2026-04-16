import json
import os

# load dataset
with open("data.json") as f:
    data = json.load(f)

def find_fix(error):
    for d in data:
        if d["error_log"] in error:
            return d["fix"]
    return None

# read error log automatically
if os.path.exists("error.log"):
    with open("error.log") as f:
        error = f.read()
else:
    print("No error log found")
    exit()

print("Detected Error:", error)

fix = find_fix(error)

if fix:
    print("Applying Fix:", fix)
    os.system(fix)  # runs pip install etc
else:
    print("No fix found")
