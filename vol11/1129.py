# -*- coding: utf-8 -*-

while True:
    n, r = list(map(int, input().split()))
    if n == 0:
        break

    cs = list(range(1, n + 1))[::-1]

    for i in range(r):
        p, c = list(map(int, input().split()))
        b = cs[p - 1:p + c - 1]
        del cs[p - 1:p + c - 1]
        cs = b + cs

    print(cs[0])
