from __future__ import print_function

#
#

'test for map'

__author__ = 'hjkruclion'

import functools
import sys
import io
import copy

def read_int():
    """Read a seris of numbers."""
    return list(map(int, sys.stdin.readline().split()))

n = read_int()[0]
a = {}
b = {}
c = {}
d = {}

for x in range(n):
    t = read_int()
    i = copy.copy(t[0])
    j = copy.copy(t[1])
    # print(i)
    a[i] = a.get(i, 0) + 1
    b[j] = b.get(j, 0) + 1
    c[i + j] = c.get(i + j, 0) + 1
    d[i - j] = d.get(i - j, 0) + 1
res = 0
for (_, x) in a.items():
    res += x * (x - 1)
for (_, x) in b.items():
    res += x * (x - 1)
for (_, x) in c.items():
    res += x * (x - 1)
for (_, x) in d.items():
    res += x * (x - 1)
print(int(res/2))

