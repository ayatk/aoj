# -*- coding: utf-8 -*-
from datetime import date

week = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

while True:
    m, d = list(map(int, input().split()))
    if m == 0:
        break

    d = date(2004, m, d)
    print(week[d.weekday()])
