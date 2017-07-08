# -*- coding: utf-8 -*-

import sys

m = []
for line in sys.stdin:
    a = list(map(int, line.split()))
    print(len(str(a[0] + a[1])))
