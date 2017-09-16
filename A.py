from __future__ import print_function
#
#

'get familiar with python'

__author__ = 'hjkruclion'

import sys
import numpy as np

def read_int():
    return list(map(int, sys.stdin.readline().split()))

P, Q, N = read_int()

def calcu(start, add):
    res = 0
    now = start
    pre = 1.0
    for i in range(10000):
        if now >= 100:
            res += pre * 1.0
            break
        res += pre
        pre = pre * (1 - now / 100.0)
        now += Q
    return res

ans = 0
if N >= 8:
    ans += calcu(0, Q) * (N - 7)
    N = 7
for i in range(1, N + 1):
    have = i - 1
    ans += calcu(int(P // int(pow(2, have) + 0.1)), Q)
print('%.2f'%(1.00))

