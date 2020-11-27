# Python program to display calendar

import calendar

month = int(input("Enter the month number (1-12) = "))
year = int(input("Enter the year number  = "))

print(calendar.month(year,month))
