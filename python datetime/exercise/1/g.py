# Write a program to check if a given date is in the past or future.
from datetime import date

year = int(input("Enter year (YYYY): "))
month = int(input("Enter month (MM): "))
day = int(input("Enter day (DD): "))

dates = date(year, month, day)

today = date.today()

if dates > today:
    print("You are in future date")

if dates < today:
    print("You are in the past")

if dates == today:
    print("This date is today")