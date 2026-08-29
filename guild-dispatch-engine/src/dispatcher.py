import json
from pathlib import Path
import guild_tools

# Defining the file paths for the JSON databases
adventurers_db = Path(__file__).parent.parent / "data" / "adventurers.json"
active_quests = Path(__file__).parent.parent / "data" / "quests.json"

# Loading the guild data into memory
with open(adventurers_db, "r") as file:
    adventurers = json.load(file)

with open(active_quests, "r") as file:
    quests = json.load(file)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
quest_schedule = {}
weekly_profit = 0

# Processing each quest and attempting to draft an available party
for quest in quests:
    quest_name = quest["quest_title"]
    target_day = quest["target_day"]
    roles_required = quest["roles_required"]

    # Querying the recruiter tool to find heroes matching the required roles
    drafted_party = guild_tools.find_party(roles_required, target_day, adventurers)

    if drafted_party is not None:
        # Marking the drafted heroes as booked for the target day
        guild_tools.book_the_party(drafted_party, target_day, adventurers)
        
        # Calculating the net profit (quest payout minus hero operational costs)
        payout = quest["reward_payout"]
        team_cost = 0
        for hero in drafted_party:
            team_cost += adventurers[hero]["operational_cost"]
            
        quest_profit = payout - team_cost
        weekly_profit += quest_profit
        
        # Saving the successful dispatch to the schedule
        team_text = ", ".join(drafted_party)
        quest_schedule[target_day] = {
            "name": quest_name,
            "team": team_text,
            "profit": quest_profit
        }
    else:
        # Logging a terminal warning if the guild lacks the required roles for the quest
        missing_roles_text = ", ".join(roles_required) 
        print(f"[!] WARNING: Missing roles for '{quest_name}' on {target_day}.")
        print(f"    Required: {missing_roles_text}\n")


# Generating the formatted CLI dispatch board
board_width = 96

print("\n" + "=" * board_width)
print("|" + " OFFICIAL GUILD DISPATCH BOARD ".center(board_width - 2) + "|")
print("=" * board_width)

# Printing column headers
headers = f"| {'DAY'.ljust(11)} | {'QUEST'.ljust(30)} | {'TEAM'.ljust(34)} | {'PROFIT'.rjust(8)} |"
print(headers)
print("-" * board_width)

# Printing the schedule row by row
for day in days:
    q_name = "Rest Day"
    team_names = "-"
    profit_str = "-"
    
    if day in quest_schedule:
        todays_data = quest_schedule[day]
        q_name = todays_data['name']
        team_names = todays_data['team']
        profit_str = f"+{todays_data['profit']}g"
        
    row = f"| {day.upper().ljust(11)} | {q_name.ljust(30)} | {team_names.ljust(34)} | {profit_str.rjust(8)} |"
    print(row)
    
    # Adding bordered spacing between days (except the last day)
    if day != "Sunday":
        empty_gap = f"|{' ' * (board_width - 2)}|"
        print(empty_gap)

# Printing the weekly financial summary
print("-" * board_width)
footer_text = f"TOTAL WEEKLY PROFIT: +{weekly_profit}g "
print(f"|{footer_text.rjust(board_width - 2)}|")
print("=" * board_width)