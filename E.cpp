#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 100 + 10;

struct node{
    int id, lson, rson, fa;
};
node t[maxn];
int n, m;

int getl(int u) {
    if(t[u].lson == -1) return u;
    return getl(t[u].lson);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int _ = 0; _ < T; _++) {
        scanf("%d%d", &n, &m);
        memset(t, 0, sizeof(t));
        for(int i = 0; i < n; i++){
            int x, y, z;
            scanf("%d%d%d", &x, &y, &z);
            t[x].lson = y;
            t[x].rson = z;
            t[z].fa = x;
            t[y].fa = x;
        }
        for(int i = 0; i < m; i++) {
            int type, x, y;
            scanf("%d", &type);
            if(type == 1) {
                scanf("%d%d", &x, &y);
                int xfa = t[x].fa, yfa = t[y].fa;
                t[x].fa = yfa;
                t[y].fa = xfa;
                int *xpos;
                int *ypos;
                if(t[xfa].lson == x) {
                    xpos = &t[xfa].lson;
                } else{
                    xpos = &t[xfa].rson;
                }
                if(t[yfa].lson == y) {
                    ypos = &t[yfa].lson;
                } else{
                    ypos = &t[yfa].rson;
                }
                int tx = (*xpos), ty = (*ypos);
                (*xpos) = ty;
                (*ypos) = tx;
            } else{
                scanf("%d", &x);
                printf("%d\n", getl(x));
            }
        }
    }
    return 0;
}
