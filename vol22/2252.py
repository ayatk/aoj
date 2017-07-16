# -*- coding: utf-8 -*-

q = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

while True:
    s = input()
    if s == '#':
        break

    c = 0
    r = False

    if s[0] in q:
        r = True

    for i in range(1, len(s)):
        if s[i] in q and not r:
            r = True
            c += 1

        if not s[i] in q and r:
            r = False
            c += 1

    print(c)
