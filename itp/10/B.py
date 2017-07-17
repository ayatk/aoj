# Introduction to Programming, Section 10, B
# Math Functions - Triangle
import math

a, b, c = list(map(float, input().split()))

# S
print("%.6f" % ((a * b * math.sin(math.radians(c))) / 2))

# L
print("%.6f" % (a + b + math.sqrt((a ** 2) + (b ** 2) - (
    2 * a * b * math.cos(math.radians(c))))))

# h
print("%.6f" % (b * math.sin(math.radians(c))))
