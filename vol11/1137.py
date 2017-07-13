# -*- coding: utf-8 -*-
import math


def mcxi_to_int(mcxi):
    tmp = 0
    num = 0
    for j in range(len(mcxi)):
        if mcxi[j].isdigit():
            tmp = int(mcxi[j])
            continue

        if mcxi[j] == 'i':
            tmp = tmp * 1 if tmp != 0 else 1
        elif mcxi[j] == 'x':
            tmp = tmp * 10 if tmp != 0 else 10
        elif mcxi[j] == 'c':
            tmp = tmp * 100 if tmp != 0 else 100
        elif mcxi[j] == 'm':
            tmp = tmp * 1000 if tmp != 0 else 1000

        num += tmp
        tmp = 0

    return num


n = int(input())

for r in range(n):
    m = input().split()
    a = mcxi_to_int(m[0]) + mcxi_to_int(m[1])
    ans = ''

    m = math.floor(a / 1000)
    a = a % 1000
    if m != 0:
        ans += (str(m) if m > 1 else '') + 'm'

    c = math.floor(a / 100)
    a = a % 100
    if c != 0:
        ans += (str(c) if c > 1 else '') + 'c'

    x = math.floor(a / 10)
    a = a % 10
    if x != 0:
        ans += (str(x) if x > 1 else '') + 'x'

    i = math.floor(a / 1)
    if i != 0:
        ans += (str(i) if i > 1 else '') + 'i'

    print(ans)
