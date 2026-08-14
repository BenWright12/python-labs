import json
from pathlib import Path

file_path1 = Path(__file__).parent.parent / "data" / "adventurers.json"
file_path2 = Path(__file__).parent.parent / "data" / "quests.json"

with open(file_path1, "r") as file:
    adventurers = json.load(file)

with open(file_path2, "r") as file:
    quests = json.load(file)

print(type(adventurers))
print(type(quests))
