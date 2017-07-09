# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    d = int(line)
    n = int(600 / d)

    s = 0
    for i in range(n):
        s += ((i * d) ** 2) * d

    print(s)
