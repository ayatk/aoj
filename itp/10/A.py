# Introduction to Programming, Section 10, A
# Math Functions - Distance
import math

x1, y1, x2, y2 = list(map(float, input().split()))

print(abs(math.hypot(x1 - x2, y1 - y2)))
