from datetime import datetime

date = "2025-02-10"

formatted_date = datetime.strptime(date, "%d-%m-%Y")
print(formatted_date)