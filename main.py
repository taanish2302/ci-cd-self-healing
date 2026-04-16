try:
    import numpy  # will fail if not installed
    print("All good")
except Exception as e:
    with open("error.log", "w") as f:
        f.write(str(e))
    raise e
