from datetime import date, datetime

exam_date = date(2026,3,10)

today = date.today()

remaining_date = (exam_date - today).days

if remaining_date > 0:
    print(f"Date remaining until your exam: {remaining_date} days")

if remaining_date == 0:
    print("To day is your exam good luck")

else:
    print("Your exam already passed out")