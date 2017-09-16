from __future__ import print_function
#
#

'python for tree and easy dp'

__author__ = 'hjkruclion'

import sys
import numpy as np

def read_int():
    return list(map(int, sys.stdin.readline().split()))

MAXN = 20000 + 10
INF = int(1e7)
MAXP = 2000 + 100

G = [[]for _ in range(MAXP)]
need = np.zeros([MAXP], np.int)
have = np.zeros([MAXP], np.int)
time = np.zeros([MAXP], np.int)


rt = 1
N = read_int()[0]
for i in range(1, N + 1):
    fa, iN, ip, c = read_int()
    if fa != 0:
        G[fa].append(i)
    else:
        rt = i
    need[i] = iN
    have[i] = ip
    time[i] = c


def dfs(u):
    if len(G[u]) == 0:
        return time[u]
    f = np.zeros([MAXN + 10], np.int)
    f[0] = 0
    for i in range(1, MAXN):
        f[i] = INF
    for i in range(len(G[u])):
        v = G[u][i]
        t = dfs(v)
        for j in reversed(range(need[u])):
            no = min(MAXN - 1, j + have[v])
            f[no] = min(INF, min(f[no], f[j] + t))
    res = INF
    for i in range(need[u], MAXN):
        res = min(res, f[i])
    return min(INF, res + time[u])

res = dfs(rt)
if res < INF:
    print(res)
else:
    print('-1')