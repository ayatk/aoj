# -*- coding: utf-8 -*-
import math

while True:
    n = int(input())
    if n == 0:
        break

    s = []
    for i in range(n):
        s.append(int(input()))

    s = sorted(s)
    del s[0], s[-1]
    print(math.trunc(sum(s) / len(s)))
