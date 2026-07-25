import json
from pathlib import Path

DATA_FILE = Path("data/data.json")


def read_json():
    print(DATA_FILE.resolve())
    print(DATA_FILE.exists())
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)
    


def write_json(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)