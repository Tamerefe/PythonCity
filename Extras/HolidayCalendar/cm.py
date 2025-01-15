import calendar
from termcolor import colored

def display_calendar():
    
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month).split('\n')

    holidays = {
        (1, 1): 'blue',  # New Year's Day
        (4, 23): 'red',  # National Sovereignty and Children's Day
        (5, 1): 'blue', # Labour and Solidarity Day
        (5, 19): 'red', # Commemoration of Atatürk, Youth and Sports Day
        (7, 15): 'blue', # Democracy and National Unity Day
        (8, 30): 'red', # Victory Day
        (10, 29): 'yellow', # Republic Day
    }

    for i, week in enumerate(month_calendar):
        for day in range(1, 32):
            if (month, day) in holidays:
                color = holidays[(month, day)]
                day_str = f"{day:2}"
                if f" {day_str} " in f" {week} ":
                    week = week.replace(day_str, colored(day_str, color))
        month_calendar[i] = week

    print('\n'.join(month_calendar))

display_calendar()