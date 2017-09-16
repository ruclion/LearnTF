#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

const int maxn = 2000 + 100;
const int MAXK = 20000 + 100;
const int INF = 1e7;

int need[maxn], have[maxn], tim[maxn];
int n, rt;
vector<int> G[maxn];

int dfs(int u) {
    if(G[u].size() == 0) return tim[u];
    int f[MAXK];
    f[0] = 0;
    for(int i = 1; i < MAXK; i++) f[i] = INF;
    for(int i = 0; i < G[u].size(); i++){
        int v = G[u][i];
        int t = dfs(v);
        for(int j = need[u] - 1; j >= 0; j--) {
            int no = min(MAXK - 1, j + have[v]);
            f[no] = min(INF, min(f[no], f[j] + t));
        }
    }
    int res = INF;
    for(int i = need[u]; i < MAXK; i++) res = min(res, f[i]);
    return res + tim[u];
}

int main() {
    scanf("%d", &n);
    rt = 1;
    for(int i = 1; i <= n; i++) G[i].clear();
    for(int i = 1; i <= n; i++) {
        int a, b, c, d;
        scanf("%d%d%d%d", &a, &b, &c, &d);
        if(a == 0){
            rt = i;
        } else{
            G[a].push_back(i);
        }
        need[i] = b;
        have[i] = c;
        tim[i] = d;
    }
    int res = dfs(rt);
    if(res < INF) printf("%d\n", res);
    else printf("-1");
}
