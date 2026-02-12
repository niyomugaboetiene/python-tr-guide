from datetime import timedelta, date

today = date.today()

future_date = today + timedelta(days=5)
print("Today", today)
print("Future date", future_date)