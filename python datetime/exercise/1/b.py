# Create a program that calculates a person’s age from their birth date.
from datetime import date
year = int(input("Enter your birth year: (YYYY)"))
month = int(input("Enter your moth birth: (MM)"))
day = int(input("Enter your birth day: (DD)"))

birth_date = date(year, month, day)
today = date.today()

age = today.year - birth_date

print(f"Your age {age} years old")