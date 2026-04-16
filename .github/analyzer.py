def find_fix(error):
    for d in data:
        if d["error_log"].lower() in error.lower():
            return d["fix"]
    return None
