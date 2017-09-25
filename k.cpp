#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>

#define lson (rt << 1)
#define rson (rt << 1 | 1)
#define Pair pair<LD, node>

using namespace std;

typedef  long double LD;

const int maxn = 50000 + 100;
const int MAXNODE = maxn * 4 + 100;
const int MAXD = 20;

int K, dim, n;

struct node{
    int a[MAXD];
    bool operator < (const node & o) const{
        return a[dim] < o.a[dim];
    }
};
LD dist(node x, node y) {
    LD ans = 0;
    for(int i = 0; i < K; i++){
        ans += (x.a[i] - y.a[i]) * (x.a[i] - y.a[i]) * 1.0;
    }
    return ans;
}
priority_queue<Pair> q;
node data[maxn], t[MAXNODE];
int tag[MAXNODE];
int m;

void build(int dep, int rt, int l, int r) {
    if(l > r) {
        return;
    }
    tag[rt] = 1;
    tag[lson] = tag[rson] = 0;
    dim = dep % K;
    int mid = (l + r) / 2;
    nth_element(data + l, data + mid, data + r + 1);
    t[rt] = data[mid];
    build(dep + 1, lson, l, mid - 1);
    build(dep + 1, rson , mid + 1, r);
}
void query(node u, int dep, int rt) {
    if(tag[rt] == 0) return;
    int u_dim = dep % K;
    int x = lson, y = rson;
    if(u.a[u_dim] > t[rt].a[u_dim]) {
        swap(x, y);
    }
    query(u, dep + 1, x);
    Pair cur;
    cur.first = dist(u, t[rt]);
    cur.second = t[rt];
    if(q.size() < m) {
        q.push(cur);
    } else {
        if(cur.first < q.top().first) {
            q.pop();
            q.push(cur);
        }
    }
    if(q.size() < m || q.top().first > (u.a[u_dim] - t[rt].a[u_dim]) * (u.a[u_dim] - t[rt].a[u_dim])) {
        query(u, dep + 1, y);
    }
}
void out() {
    printf("the closest %d points are:\n", m);
    node st[MAXD];
    int ans = q.size();
    for(int i = 0; i < ans; i++) {
        st[i] = q.top().second;
        q.pop();
    }
    for(int i = ans - 1; i >= 0; i--) {
        for(int j = 0; j < K; j++) {
            printf("%d%c", st[i].a[j], (j == K - 1 ? '\n' : ' '));
        }
    }
}

int main(){
    while(scanf("%d %d", &n, &K) != EOF){
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j < K; j++) {
                scanf("%d", &data[i].a[j]);
            }
        }
        build(0, 1, 1, n);
        int t;
        scanf("%d", &t);
        for(int i = 1; i <= t; i++) {
            while(!q.empty()) q.pop();
            node tmp;
            for(int j = 0; j < K; j++) {
                scanf("%d", &tmp.a[j]);
            }
            scanf("%d", &m);
            query(tmp, 0, 1);
            out();
        }
    }
    return 0;
}
