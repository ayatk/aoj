# -*- coding: utf-8 -*-
import math

n = int(input())

for i in range(n):
    s = sorted(list(map(int, input().split())))
    print("YES" if (math.hypot(s[0], s[1]) == s[2]) else "NO")
