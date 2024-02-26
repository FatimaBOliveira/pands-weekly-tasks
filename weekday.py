# Weekday
# Program that outputs if today is a weekday or a day in weekend.
#Author: Fatima Oliveira

from datetime import date  # Will export today's time # https://realpython.com/python-datetime/
# https://www.w3schools.com/python/python_datetime.asp

today = date.today() # https://docs.python.org/3/library/datetime.html#datetime.date.today

if today.weekday() == 0:  #https://docs.python.org/3/library/datetime.html#datetime.date.weekday
    # 0 is correspondent to Monday, then 1 to Tuesday, then 2 to Wednesday, 3 to Thursday and 4 to Friday
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 1:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 2:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 3:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 4:
    print("Yes, unfortunately today is a weekday.")
else: # Values above 4 are weekend days
    print("It is the weekend, yay!")