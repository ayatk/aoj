# -*- coding: utf-8 -*-

while True:
    n, m, a = list(map(int, input().split()))
    if n == 0:
        break

    b = list(range(1, n + 1))
    w = []
    for i in range(m):
        w.append(list(map(int, input().split())))

    w = sorted(w)

    for j in range(m):
        b[w[j][1] - 1], b[w[j][2] - 1] = b[w[j][2] - 1], b[w[j][1] - 1]

    print(b[a-1])
