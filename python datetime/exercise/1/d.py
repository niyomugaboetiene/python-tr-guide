# Convert a given string date ("2026-02-10") into a datetime object.
from datetime import datetime

date = "2026-02-12"

date_obj  = datetime.strptime(date, "%Y-%m-%d")

print(date)