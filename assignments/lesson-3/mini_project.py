# Mini-Project: Day Planner
 
day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()
 
if day not in ("monday", "tuesday", "saturday"):
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Saturday...")
elif time not in ("morning", "afternoon", "evening"):
    print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")
elif day == "monday":
    if time == "morning":
        print("Suggestion: Plan out your week and set three goals.")
    elif time == "afternoon":
        print("Suggestion: Knock out your toughest task while you're fresh.")
    else:
        print("Suggestion: Take a walk and unwind from the first day back.")
elif day == "tuesday":
    if time == "morning":
        print("Suggestion: Morning Python class — great time to focus!")
    elif time == "afternoon":
        print("Suggestion: Practice what you learned with a small coding exercise.")
    else:
        print("Suggestion: Catch up with a friend over dinner.")
else:  # saturday
    if time == "morning":
        print("Suggestion: Sleep in, then make a big breakfast.")
    elif time == "afternoon":
        print("Suggestion: Head to a park or explore somewhere new in town.")
    else:
        print("Suggestion: Perfect night for a movie or trying a new recipe.")
 