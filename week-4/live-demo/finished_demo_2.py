apps = [
    {"app": "Instagram", "minutes": 95,  "type": "Social"},
    {"app": "VS Code",   "minutes": 180, "type": "Work"},
    {"app": "YouTube",   "minutes": 70,  "type": "Fun"},
    {"app": "Slack",     "minutes": 45,  "type": "Work"},
    {"app": "TikTok",    "minutes": 60,  "type": "Social"},
    {"app": "Spotify",   "minutes": 130, "type": "Music"},
    {"app": "Chrome",    "minutes": 110, "type": "Work"},
    {"app": "WhatsApp",  "minutes": 40,  "type": "Social"},
    {"app": "Netflix",   "minutes": 85,  "type": "Fun"},
    {"app": "Gmail",     "minutes": 30,  "type": "Work"},
    {"app": "Reddit",    "minutes": 55,  "type": "Social"},
    {"app": "Duolingo",  "minutes": 20,  "type": "Learning"},
    {"app": "Maps",      "minutes": 15,  "type": "Utility"},
    {"app": "Twitch",    "minutes": 75,  "type": "Fun"},
    {"app": "Notion",    "minutes": 50,  "type": "Work"},
]

# Set up every accumulator BEFORE the loop
top_app = None
top_minutes = 0
total = 0
categories = set()
time_sinks = []

# One pass — update all four in the same loop
for entry in apps:
    if entry["minutes"] > top_minutes:      # 1. track the max
        top_minutes = entry["minutes"]
        top_app = entry["app"]

    total += entry["minutes"]               # 2. accumulate the sum

    categories.add(entry["type"])           # 3. collect unique categories

    if entry["minutes"] > 60:               # 4. filter the time-sinks
        time_sinks.append(entry["app"])

average = total / len(apps)                 # divide once, after the loop

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