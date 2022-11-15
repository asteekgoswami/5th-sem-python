#  Write a program to print day of a month

import calendar

month=int(input("enter the month : "))
year=int(input("enter the year : "))
print(calendar.month(year,month))