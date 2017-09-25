#
#

'f'

__author__ = 'hjkruclion'

import sys

def read_int():
    return list(map(int, sys.stdin.readline().split()))
def read_str():
    return sys.stdin.readline().split()[0]

maxn = 100000 + 100
MAXNUM = 27
INF = int(1e8)

f = [[INF for j in range(MAXNUM)] for i in range(maxn)]
h = [[0 for j in range(MAXNUM)] for i in range(MAXNUM)]

def no(ch):
    return ord(ch) - ord('a')
# print(no('a'))
N = read_int()[0]
t = read_str()
s = ['a' for _ in range(maxn)]
for i in range(1, N + 1):
    s[i] = t[i - 1]
M = read_int()[0]
for i in range(1, M + 1):
    t = read_str()
    h[no(t[0])][no(t[1])] = 1
    h[no(t[1])][no(t[0])] = 1

f[0][26] = 0
for i in range(1, N + 1):
    t = no(s[i])
    for j in range(0, 27):
        f[i][j] = min(f[i][j], f[i - 1][j] + 1)
    for j in range(0, 27):
        if h[t][j] == 0:
            f[i][t] = min(f[i][t], f[i - 1][j])
res = INF
for i in range(0, 27):
    res = min(res, f[N][i])
print(res)