import json

with open("data.json") as f:
    data = json.load(f)

def auto_fix(error):
    for d in data:
        if d["error_log"] in error:
            return d["fix"]
    return "No fix found"

# simulate pipeline error
error = "ModuleNotFoundError: No module named 'numpy'"

print("Detected Error:", error)
print("Suggested Fix:", auto_fix(error))
