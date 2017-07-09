# -*- coding: utf-8 -*-

n = int(input())

a = 0
un = 0
for i in range(n):
    inp = input()

    if inp == 'A':
        a += 1
    if inp == 'Un':
        un += 1

    if a < un:
        print('NO')
        exit(0)

if a != un:
    print('NO')
elif un != 0:
    print('YES')
