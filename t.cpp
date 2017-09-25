#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

const int maxN = 10000 + 100;
const int maxC = 100 + 10;

struct node{
    int t, s_no, now_id, id;
    node(int _t, int _s_no, int _now_id, int _id) {
        t = _t;
        s_no = _s_no;
        now_id = _now_id;
        id = _id;
    }
    bool operator < (const node &o) const {
        if(t == o.t) {
            return s_no > o.s_no;
        }
        return t > o.t;
    }
};

priority_queue<node> q;
int N, M, K;
int c_tim[maxC], p[maxN], ans[maxN];
int s[maxN][maxC][2];

int main() {
    scanf("%d%d%d", &N, &M, &K);
    while(!q.empty()) q.pop();
    memset(c_tim, 0, sizeof(c_tim));
    for(int i = 1; i <= N; i++) {
        int si, ti;
        scanf("%d%d%d", &si, &ti, &p[i]);
        for(int j = 1; j <= p[i]; j++) {
            scanf("%d%d", &s[i][j][0], &s[i][j][1]);
        }
        q.push(node(ti, si, 1, i));
    }
    while(!q.empty()) {
        node u = q.top();
        q.pop();
        int start_t = max(c_tim[s[u.id][u.now_id][0]], u.t);
        int end_t = start_t + s[u.id][u.now_id][1];
        c_tim[s[u.id][u.now_id][0]] = end_t;
        if(u.now_id == p[u.id]) {
            ans[u.id] = end_t;
        } else{
            q.push(node(end_t + K, u.s_no, u.now_id + 1, u.id));
        }
    }
    for(int i = 1; i <= N; i++) printf("%d\n", ans[i] + K);
    return 0;
}
