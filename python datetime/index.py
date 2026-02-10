from datetime import datetime
from datetime import date

now = datetime.now()
print(f"Now {now}")

# get only date
today = date.today()
print(f"To day {today}")

print(today.month)
print(today.year)
print(today.day)