# Introduction to Programming, Section 10, B
# Math Functions - Standard Deviation
import math

while True:
    n = int(input())
    if not n:
        break
    s = list(map(float, input().split()))
    m = sum(s) / n

    print(math.sqrt(sum([(s[i] - m) ** 2 for i in range(n)]) / n))
