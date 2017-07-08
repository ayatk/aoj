a = []
while True:
    n = int(input())
    if n == 0:
        break
    a = sorted(list(map(int, input().split())))
    diff = abs(a[0] - a[1])
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) < diff:
            diff = abs(a[i] - a[i + 1])
    print(diff)
