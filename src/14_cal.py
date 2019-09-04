"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

#datetime.now() returns current local time and date

def cal(*args):
    try:
        #get sys.argv length
        args = len(sys.argv)
        #get current month
        month = datetime.now().month
        #get current year
        year = datetime.now().year

        if args == 1:
            print()
        if args == 2:
        if args == 3:
    except:
        print("usage expected: calendar.py [month] [year]")

cal()


'''print(calendar.weekheader(3))
'''#letters per weekday header

'''print(calendar.firstweekday())
'''#whats the first day of the week? 0 = Monday 1 = Tuesday etc.

'''print(calendar.month(2019, 9, w=3))
'''#the whole month, with month and year - add a arg for w = weekheader letter qty

'''print(calendar.monthcalendar(2019, 9))
'''#matrix, two dimensional array of arrays of wach week in a month where 0 = not a day that month (useful if you need calculations on dates (schedule your computer to run the script to automate this thing to hack your friend to text your friend etc ))

'''print(calendar.calendar(2019))'''
#prints the entire freaking year

#aim for self-commenting code!  check the holidays of the future!
'''day_of_the_week = calendar.weekday(2020, 7, 3)
print(day_of_the_week)'''


'''is_leapyear = calendar.isleap(2024)
print(is_leapyear)'''
# leapyear is every 4 years, usually

'''how_many_leap_days = calendar.leapdays(2001, 2029)
print(how_many_leap_days)'''
# count the leapdays between two years, excludes the last year so always go one over the year you want 