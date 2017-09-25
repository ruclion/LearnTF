from __future__ import print_function
#
#

'interpret'

__author__ = 'hjkruclion'

maxn = 30
maxnLen = 1e5

a = [[] for i in range(maxn)]
flag = [[] for i in range(maxn)]
cTOn = [0 for i in range(1000)]
has = [0 for i in range(1000)]
import sys

def read_int():
    return list(map(int, sys.stdin.readline().split()))

def read_str():
    return sys.stdin.readline().split()[0]

def read_white_str():
    return sys.stdin.readline().split()

def isdigit(ch):
    if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
        return True
    return False
def changeA(t):
    if isinstance(t, int):
        return t
    return cTOn[ord(t)]

cnt = 0
N = read_int()[0]
for i in range(N):
    t = read_str()
    l = len(t)
    j = 0
    while(j < l):
        if t[j] == '<' and t[j + 1] != '=':
            flag[i].append(1)
            j += 1
        elif t[j] == '<' and t[j + 1] == '=':
            flag[i].append(2)
            j += 2
        elif isdigit(t[j]):
            k = j
            while(k < l and isdigit(t[k])):
                k += 1
            num = int(t[j:k])
            a[i].append(num)
            j = k
        else:
            if has[ord(t[j])] == 0:
                has[ord(t[j])] = 1
                cnt += 1
            a[i].append(t[j])
            j += 1
T = read_int()[0]
for _ in range(T):
    for i in range(cnt):
        t = read_white_str()
        cTOn[ord(t[0][0])] = int(t[1])
    ans = 1
    for i in range(N):
        l = len(a[i])
        for j in range(1, l):
            x = changeA(a[i][j - 1])
            y = changeA(a[i][j])
            if flag[i][j - 1] == 1:
                if y <= x:
                    ans = 0
                    break
            if flag[i][j - 1] == 2:
                if y < x:
                    ans = 0
                    break
    if ans == 1:
        print('Yes')
    else:
        print('No')


