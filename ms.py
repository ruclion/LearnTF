from __future__ import print_function
#
#

'dfs and math'

__author__ = 'hjkruclion'

import sys
import math

def read_int():
    return list(map(int, sys.stdin.readline().split()))
def read_str():
    return sys.stdin.readline().split()[0]

maxn = 500 + 100
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def dcmp(x):
    if math.fabs(x) < 1e-4:
        return 0
    if x > 0:
        return 1
    return -1

a = [['.' for j in range(maxn)] for i in range(maxn)]
vis = [[0 for j in range(maxn)] for i in range(maxn)]
G = []

N, M = read_int()

for i in range(N):
    a[i] = read_str()
    # for j in range(M):
    #     a[i][j] = t[j]
    # if i <= 5:
    #     print(len(a[i]))

# print(a[7][7] == '#')

resM = 0
resS = 0

def calcu(x, y, x1, y1, x2, y2):
    if x1 == x2:
        if dcmp((x1 - x)) == 0:
            return 1
        elif dcmp((x1 - x)) > 0:
            return 1
        else:
            return -1

    else:
        t = (y2 - y1) / (x2 - x1) * (x - x1) + y1 - y
        if dcmp(t) > 0:
            return 1
        elif dcmp(t) == 0:
            return 1
        else:
            return -1

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def bfs(xs, ys, tag):
    global G, vis
    q = [(xs, ys)]
    vis[xs][ys] = tag
    ansx = xs
    ansy = ys
    if tag == 1:
        G.append((xs, ys))
    while(len(q) != 0):
        x, y = q.pop(0)
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and vis[nx][ny] != tag and a[nx][ny] == '#':
                q.append((nx, ny))
                vis[nx][ny] = tag
                if tag == 1:
                    G.append((nx, ny))
                ansx = nx
                ansy = ny
    return ansx, ansy

for i in range(N):
    for j in range(M):
        if vis[i][j] != 0 or a[i][j] == '.':
            continue
        # print('hh')
        G = []
        x1, y1 = bfs(i, j, 1)
        x2, y2 = bfs(x1, y1, 2)
        num = len(G)
        ans = 0
        zx = 0
        zy = 0
        for _ in range(num):
            # ans += calcu(G[_][0], G[_][1], x1, y1, x2, y2)
            zx += G[_][0]
            zy += G[_][1]
        zx /= num
        zy /= num
        dist1 = dist(zx, zy, (x1 + x2) / 2, (y1 + y2) / 2)
        dist2 = dist(x1, y1, x2, y2)
        if dist1 / (dist2 / 2) >= 0.5:
            resM += 1
        else:
            resS += 1
        # if math.fabs(ans) >= num / 2:
        #     resM += 1
        # else:
        #     resS += 1
print(resM, resS)