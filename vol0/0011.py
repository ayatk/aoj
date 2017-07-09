# -*- coding: utf-8 -*-

n = list(range(1, int(input()) + 1))
w = int(input())

for i in range(w):
    a, b = list(map(int, input().split(',')))
    n[a - 1], n[b - 1] = n[b - 1], n[a - 1]

[print(s) for s in n]
