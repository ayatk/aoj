# -*- coding: utf-8 -*-

l = [
    ['.', ',', '!', '?', ' '],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z'],
]

n = int(input())
for i in range(n):
    a = list(filter(lambda s: s != '', input().split('0')))
    o = []
    for j in range(len(a)):
        o.append(l[int(a[j][0]) - 1][len(a[j]) % len(l[int(a[j][0]) - 1]) - 1])

    print(''.join(o))
