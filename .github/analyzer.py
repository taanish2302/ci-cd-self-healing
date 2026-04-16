import json

with open("data.json") as f:
    data = json.load(f)

for d in data:
    print("Error:", d["error_log"])
    print("Suggested Fix:", d["fix"])
    print("-" * 40)
