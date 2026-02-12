from datetime import datetime

date = datetime.today()

formatted_date = datetime.strptime(date, "%d-%m-%Y")
print(formatted_date)