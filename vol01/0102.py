# Volume1, No.2
# Matrix-like Computation

while True:
    n = int(input())
    if not n:
        break

    m = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        m[i].append(sum(m[i]))

    s = []

    for i in range(n + 1):
        s.append(sum([m[j][i] for j in range(n)]))
    m.append(s)

    print('\n'.join([
        ''.join(["%5d" % m[i][j] for j in range(n + 1)]) for i in range(n + 1)
    ]))
