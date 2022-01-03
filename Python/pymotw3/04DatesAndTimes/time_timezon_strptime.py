#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""time_timezon_strptime
@Author: yongliang
@License: MIT
"""

import time
import os


print('\n---- timezon ----')


def show_zone_info():
    print('  TZ    :', os.environ.get('TZ', '(not set)'))
    print('  tzname:', time.tzname)
    print('  Zone  : {} ({})'.format(
        time.timezone, (time.timezone / 3600)))
    print('  DST   :', time.daylight)
    print('  Time  :', time.ctime())
    print()


print('Default :')
show_zone_info()

ZONES = [
    'GMT',
    'Europe/Amsterdam',
    'Asia/Shanghai'
]

for zone in ZONES:
    os.environ['TZ'] = zone
    time.tzset()
    print(zone, ':')
    show_zone_info()


print('\n---- strptime ----')


def show_struct(s):
    print('  tm_year :', s.tm_year)
    print('  tm_mon  :', s.tm_mon)
    print('  tm_mday :', s.tm_mday)
    print('  tm_hour :', s.tm_hour)
    print('  tm_min  :', s.tm_min)
    print('  tm_sec  :', s.tm_sec)
    print('  tm_wday :', s.tm_wday)
    print('  tm_yday :', s.tm_yday)
    print('  tm_isdst:', s.tm_isdst)


now = time.ctime(1483391847.433716)
print('Now:', now)

parsed = time.strptime(now)
print('\nParsed:')
show_struct(parsed)

print('\nFormatted:',
      time.strftime("%a %b %d %H:%M:%S %Y", parsed))