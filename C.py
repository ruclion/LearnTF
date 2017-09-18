#
#

'test python speed'

__author__ = 'hjkruclion'

import sys

def read_int():
    return list(map(int, sys.stdin.readline().split()))
def read_str():
    return sys.stdin.readline().split()[0]

maxn = 20 + 5
MAXSTA = (1 << 20) + 100
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mp = [['.' for j in range(maxn)] for i in range(maxn)]
t_mp = [[0 for j in range(maxn)] for i in range(maxn)]
no_mp = [[0 for j in range(maxn)] for i in range(maxn)]
vis = [[0 for j in range(maxn)] for i in range(maxn)]
in_Hi = [0 for i in range(maxn)]
in_Ai = [0 for i in range(maxn)]
f = [[0 for j in range(7)] for i in range(MAXSTA)]

Di = Dj = 0
N, M = read_int()
key = (1 << (N * M))
no = 0
# print(N, M)
for i in range(N):
    t = read_str()
    for j in range(M):
        mp[i][j] = t[j]
        if mp[i][j] == 'S' or mp[i][j] == 'M':
            no_mp[i][j] = no
            no += 1
        if mp[i][j] == 'D':
            Di = i
            Dj = j
for i in range(no):
    in_Hi[i], in_Ai[i] = read_int()
in_Hp, in_Ap = read_int()

def changeToMat(sta):
    global t_mp
    for x in range(0, N):
        for y in range(0, M):
            t = getSta(x, y)
            if (sta & t) != 0:
                t_mp[x][y] = 1
            else:
                t_mp[x][y] = 0

def logic(x, y):
    if x < N and x >= 0 and y < M and y >= 0:
        return True
    return False

def dfs(x, y):
    ans = 1
    global t_mp, vis
    vis[x][y] = 1
    for k in range(4):
        tx = x + dx[k]
        ty = y + dy[k]
        if logic(tx, ty) and vis[tx][ty] == 0 and t_mp[tx][ty] == 1:
            ans += dfs(tx, ty)
    return ans

def check():
    global t_mp, vis
    cnt = 0
    for x in range(0, N):
        for y in range(0, M):
            vis[x][y] = 0
            if t_mp[x][y] == 1:
                cnt += 1

    t = dfs(Di, Dj)
    if t == cnt:
        return True
    else:
        return False

def getSta(x, y):
    return (1 << (x * M +  y))

def hasNei(x, y):
    global t_mp
    for k in range(4):
        tx = x + dx[k]
        ty = y + dy[k]
        if logic(tx, ty) and t_mp[tx][ty] == 1:
            return True
    return False


f[getSta(Di, Dj)][5] = in_Hp
# print(in_Hp)
for sta in range(key):
    # print(sta)
    changeToMat(sta)
    if not check():
        continue
    for r in range(6):
        if f[sta][r] == 0:
            continue
        for x in range(N):
            for y in range(M):
                if not hasNei(x, y) or ((getSta(x, y)&sta) != 0):
                    continue
                if mp[x][y] == '.':
                    nsta = sta | getSta(x, y)
                    nr = max(0, r - 1)
                    f[nsta][nr] = max(f[nsta][nr], f[sta][r])
                else:
                    r_ = max(0, r - 1)
                    Hi = in_Hi[no_mp[x][y]]
                    Ai = in_Ai[no_mp[x][y]]
                    Hp = f[sta][r]
                    Ap = in_Ap
                    if r_ * Ap >= Hi:
                        nr = r_ - (Hi + Ap - 1) // Ap
                        nsta = sta | getSta(x, y)
                        if mp[x][y] == 'S':
                            nr = 5
                        f[nsta][nr] = max(f[nsta][nr], f[sta][r])
                    else:
                        nr = 0
                        nsta = sta | getSta(x, y)
                        Hi_ = Hi - r_ * Ap
                        # print(Hi_, Hp)
                        Hp_ = Hp - (Hi_ + Ap - 1) // Ap * Ai
                        # print('now:', Hi_, Hp_)
                        if mp[x][y] == 'S':
                            # print(Hp_, x, y)
                            nr = 5
                        f[nsta][nr] = max(f[nsta][nr], Hp_)

res = 0
for i in range(6):
    res = max(res, f[key - 1][i])
if res == 0:
    print('DEAD')
else:
    print(res)
