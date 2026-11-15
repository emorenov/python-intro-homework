from datetime import datetime

now = datetime.now()
date = now.strftime("%B %d, %Y")
print(f"Today is {date}")