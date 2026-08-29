# Recruiter defintion - returns a list of available heros for each role required, returns None if it fails
def find_party(roles_required, day, roster):
    drafted_party = []

    for required_role in roles_required:
        role_filled = False
        for name, stats in roster.items():
            if stats["role"] == required_role and day in stats["available_days"] and name not in drafted_party:
                drafted_party.append(name)
                role_filled = True
                break 
        if role_filled == False:
            return None 
    return drafted_party

# Double booked blocker function - will remove the day from thier availability once they are booked
def book_the_party(drafted_party, day, roster):
    for hero in drafted_party:
        roster[hero]["available_days"].remove(day)