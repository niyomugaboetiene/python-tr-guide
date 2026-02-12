from datetime import datetime

date = datetime.today()

formatted_date = datetime.strftime(date, "%d-%m-%Y")
print(formatted_date)