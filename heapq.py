from __future__ import print_function
#
#

'test for heapq'

__author__ = 'hjkruclion'

import heapq
import sys

def read_int():
     return list(map(int, sys.stdin.readline().split()))

maxC = 100 + 10
maxN = 10000 + 100

N, M, K = read_int()

c_tim = [0 for i in range(maxC)]
s = [[(0, 0) for j in range(maxC)] for i in range(maxN)]
p = [0 for i in range(maxN)]
ans = [0 for i in range(maxN)]

h = []

for i in range(1, N + 1):
    t = read_int()
    si, ti, p[i] = t[0 : 3]
    for j in range(1, p[i] + 1):
        s[i][j] = (t[j * 2 - 2 + 3], t[j * 2 + 1 - 2 + 3])
    heapq.heappush(h, (ti, si, 1, i))

while len(h) > 0:
    (t_u, s_no_u, now_id_u, id_u) = heapq.heappop(h)
    now_c_id , now_c_tim = s[id_u][now_id_u]
    start_t = max(c_tim[now_c_id], t_u)
    end_t = start_t + now_c_tim
    c_tim[now_c_id] = end_t
    if now_id_u == p[id_u]:
        ans[id_u] = end_t
    else:
        get_t = end_t + K
        heapq.heappush(h, (get_t, s_no_u, now_id_u + 1, id_u))

for i in range(1, N + 1):
    print(ans[i] + K)

