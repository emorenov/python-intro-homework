apps = [
    {"app": "Instagram", "minutes": 95,  "type": "Social"}, # 0 
    {"app": "VS Code",   "minutes": 180, "type": "Work"}, # 1
    {"app": "YouTube",   "minutes": 70,  "type": "Fun"},
    {"app": "Slack",     "minutes": 45,  "type": "Work"},
    {"app": "TikTok",    "minutes": 60,  "type": "Social"},
    {"app": "Spotify",   "minutes": 130, "type": "Music"},
    {"app": "Chrome",    "minutes": 110, "type": "Work"},
    {"app": "WhatsApp",  "minutes": 40,  "type": "Social"},
    {"app": "Netflix",   "minutes": 85,  "type": "Fun"},
    {"app": "Gmail",     "minutes": 30,  "type": "Work"},
    {"app": "Reddit",    "minutes": 55,  "type": "Social"}, # 10
    {"app": "Duolingo",  "minutes": 20,  "type": "Learning"}, # 11
    {"app": "Maps",      "minutes": 15,  "type": "Utility"},
    {"app": "Twitch",    "minutes": 20,  "type": "Fun"},
    {"app": "Notion",    "minutes": 50,  "type": "Work"}, #
]

# 1. Most-used app — track the highest minutes and the app name that goes with it
top_app = None
top_minutes = 0
for index, entry in enumerate(apps):
    # compare this app's minutes to the best so far; if bigger, update both
    
    if entry["minutes"] > top_minutes: # 0, 95, 180, 
        top_minutes = entry["minutes"]
        top_app = entry["app"]          # None, Instagram, , VS Code


# += 
# top_minutes += 10
# top_minutes = top_minutes + 10

# 2. Average minutes — add up all the minutes, then divide by how many apps
total = 0
for entry in apps:
    # add this app's minutes to the running total
    total += entry["minutes"] # 0, 95, 180 + 95, + 70


average = total / len(apps)  # replace with total / len(apps)


# 3. Unique categories — add each type to a set (duplicates ignored automatically)
categories = set()
for entry in apps:
    # add this app's type to the set
    categories.add(entry["type"])



# 4. Time-sinks over 60 min — collect the names of apps above the threshold
time_sinks = []
for entry in apps:
    # if this app's minutes are over 60, append its name
    if entry["minutes"] > 60:
        time_sinks.append(entry["app"]) # [], Instagram, VS Code, YouTube,



# Convert total minutes into hours + minutes
hours = total // 60      # // floor division: how many whole hours fit
minutes = total % 60     # %  modulo: the leftover minutes


print("=" * 45)
print("  SCREEN TIME REPORT")
print("=" * 45)
print(f"Most-used app:     {top_app} ({top_minutes} min)")
print(f"Total screen time: {hours}h {minutes}m")
print(f"Average per app:   {average:.1f} min")
print(f"Categories:        {categories}")
print(f"Time-sinks (>60):  {time_sinks}")
print("=" * 45)