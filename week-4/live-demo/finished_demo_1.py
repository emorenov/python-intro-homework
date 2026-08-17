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

# 1. Most-used app — manual max-tracking
top_app = None
top_minutes = 0
for entry in apps:
    if entry["minutes"] > top_minutes:
        top_minutes = entry["minutes"]
        top_app = entry["app"]

# 2. Average minutes — accumulate, then divide
total = 0
for entry in apps:
    total += entry["minutes"]
average = total / len(apps)

# 3. Unique categories — collect into a set
categories = set()
for entry in apps:
    categories.add(entry["type"])

# 4. Time-sinks over 60 min — filter with a loop and .append()
time_sinks = []
for entry in apps:
    if entry["minutes"] > 60:
        time_sinks.append(entry["app"])

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