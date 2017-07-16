# -*- coding: utf-8 -*-

count = 1
while True:
    n = int(input())
    if n == 0:
        break

    x = []
    y = []
    for i in range(n):
        t = list(map(int, input().split()))
        x.append(t[0])
        y.append(t[1])

    pol = 0.0
    for j in range(n - 1):
        pol += x[j] * y[j + 1] - x[j + 1] * y[j]

    pol += x[n - 1] * y[0] - x[0] * y[n - 1]

    if pol < 0:
        pol *= -1

    print("%d %.1f" % (count, pol / 2))
    count += 1
    input()  # 入れないとおちる
