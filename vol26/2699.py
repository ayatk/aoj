# -*- coding: utf-8 -*-
import math

while True:
    d, e = list(map(int, input().split()))
    if not d:
        break

    m_set = []
    for i in range(int((d / 2) + 1)):
        m_set.append(abs(math.hypot(d - i, i) - e))

    print(min(m_set))
