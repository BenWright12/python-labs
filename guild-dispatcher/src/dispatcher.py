import json
from pathlib import Path

# imported both json files to pull data from
file_path1 = Path(__file__).parent.parent / "data" / "adventurers.json"
file_path2 = Path(__file__).parent.parent / "data" / "quests.json"

with open(file_path1, "r") as file:
    adventurers = json.load(file)

with open(file_path2, "r") as file:
    quests = json.load(file)


# Example - for loop in a dictionary
# for name, stats in adventurers.items():
    # 'name' is the key (e.g., "Borg")
    # 'stats' is the inner dictionary
#    char_class = stats["class"]
#    print(f"{name} is a {char_class}")

# Example - for loop in lists
# for quest in quests:
    # must loop through the list of lists
    # then variable the section you want to target to loop through 
#    target_day = quest["target_day"]
#    name = quest["quest_title"]
#    if target_day == "Tuesday":
#        print(f"{name} is on a {target_day}")

