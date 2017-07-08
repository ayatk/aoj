# -*- coding: utf-8 -*-

n = int(input())

u = []
for i in range(n):
    u.append(input())

m = int(input())
is_opend = False

for j in range(m):
    t = input()
    msg = ''
    if t in u:
        msg += 'Closed by ' if is_opend else 'Opened by '
        is_opend = not is_opend
    else:
        msg += 'Unknown '

    print(msg + t)
