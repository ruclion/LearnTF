from __future__ import print_function
#
#

'easy'

__author__ = 'hjkruclion'

import sys
import math

def read_int():
    return list(map(int, sys.stdin.readline().split()))
def read_str():
    return sys.stdin.readline().split()[0]

N = read_int()[0]
a = read_int()
cnt = 0
for i in range(N):
    if a[i] % 2 == 0:
        cnt += 1
    else:
        cnt -= 1
print(int(math.fabs(cnt) + 0.1))