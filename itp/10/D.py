# Introduction to Programming, Section 10, B
# Math Functions - Standard Deviation


def minc_dist(x, y, p):
    if p == float('inf'):
        return max([abs(x[i] - y[i]) for i in range(len(x))])

    return sum([abs(x[i] - y[i]) ** p for i in range(len(x))]) ** (1 / p)


n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

print(minc_dist(x, y, 1))
print(minc_dist(x, y, 2))
print(minc_dist(x, y, 3))
print(minc_dist(x, y, float('inf')))
