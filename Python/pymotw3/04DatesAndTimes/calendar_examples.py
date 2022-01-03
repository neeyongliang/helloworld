#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""calendar_examples
@Author: yongliang
@License: MIT
"""

import calendar
import pprint
import sys

print('---- textcalendar ----')
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2017, 7)

print('\n---- formatyear ----')
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(2018, 2, 1, 1, 3))

print('\n---- locale ----')
c = calendar.LocaleTextCalendar(locale='en_US')
c.prmonth(2018, 5)

print()

c = calendar.LocaleTextCalendar(locale='zh_CN')
c.prmonth(2018, 5)

print('\n---- monthcalendar ----')
pprint.pprint(calendar.monthcalendar(2018, 5))

print('\n---- secondthursday ----')
year = 2018

# Show every month
for month in range(1, 13):

    # Compute the dates for each week that overlaps the month
    c = calendar.monthcalendar(year, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    # If there is a Thursday in the first week,
    # the second Thursday is in the second week.
    # Otherwise, the second Thursday must be in
    # the third week.
    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]

    print('{:>3}: {:>2}'.format(calendar.month_abbr[month],
                                meeting_date))
