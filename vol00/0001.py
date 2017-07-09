import sys

m = []
for line in sys.stdin:
    m.append(int(line))

for i in range(3):
    print(sorted(m, reverse=True)[i])
