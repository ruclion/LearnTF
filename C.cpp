#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 20 + 5;
const int MAXSTA = (1 << 20) + 100;
int dx[5] = {-1, 0, 1, 0};
int dy[5] = {0, 1, 0, -1};

int t_mp[maxn][maxn], no_mp[maxn][maxn], vis[maxn][maxn], in_Hi[maxn], in_Ai[maxn], f[MAXSTA][10];
char mp[maxn][maxn];
int Di, Dj;
int N, M, key, no;
int in_Hp, in_Ap;

int getSta(int x, int y) {
    return (1 << (x * M + y));
}

void changeToMat(int sta) {
    memset(t_mp, 0, sizeof(t_mp));
    for(int x = 0; x < N; x++) {
        for(int y = 0; y < M; y++){
            int t = getSta(x, y);
            if((sta & t) != 0) {
                t_mp[x][y] = 1;
            }
        }
    }
}

int logic(int x, int y){
    if (x < N && x >= 0 && y < M && y >= 0) return 1;
    return 0;
}

int dfs(int x, int y){
    int ans = 1;
    vis[x][y] = 1;
    for(int k = 0; k < 4; k++){
        int tx = x + dx[k], ty = y + dy[k];
        if(logic(tx, ty) && vis[tx][ty] == 0 and t_mp[tx][ty] == 1) {
            ans += dfs(tx, ty);
        }
    }
    return ans;
}

int check() {
    int cnt = 0;
    for(int x = 0; x < N; x++) {
        for(int y = 0; y < M; y++) {
            if(t_mp[x][y] == 1) cnt++;
        }
    }
    memset(vis, 0, sizeof(vis));
    int t = dfs(Di, Dj);
    if(t == cnt) return 1;
    return 0;
}

int hasNei(int x, int y) {
    for(int k = 0; k < 4; k++) {
        int tx = x + dx[k], ty = y + dy[k];
        if(logic(tx, ty) && t_mp[tx][ty] == 1) return 1;
    }
    return 0;
}
int main(){
    scanf("%d%d", &N, &M);
    key = (1 << (N * M));
    no = 0;
    for(int i = 0; i < N; i++) {
        scanf("%s", mp[i]);
        for(int j = 0; j < M; j++){
            if(mp[i][j] == 'S' || mp[i][j] == 'M') {
                no_mp[i][j] = no;
                no += 1;
            }
            if(mp[i][j] == 'D') {
                Di = i;
                Dj = j;
            }
        }
    }
    for(int i = 0; i < no; i++){
        scanf("%d%d", &in_Hi[i], &in_Ai[i]);
    }
    scanf("%d%d", &in_Hp, &in_Ap);
    memset(f, 0, sizeof(f));
    f[getSta(Di, Dj)][5] = in_Hp;
    for(int sta = 0; sta < key; sta++) {
        changeToMat(sta);
        if(check() == 0) {
            continue;
        }
        for(int r = 0; r <= 5; r++) {
            if(f[sta][r] == 0) continue;
            for(int x = 0; x < N; x++) {
                for(int y = 0; y < M; y++) {
                    if(hasNei(x, y) == 0 || ((getSta(x, y)&sta) != 0)) continue;
                    if(mp[x][y] == '.') {
                        int nsta = sta | getSta(x, y);
                        int nr = max(0, r - 1);
                        f[nsta][nr] = max(f[nsta][nr], f[sta][r]);
                    } else{
                        int r_ = max(0, r - 1);
                        int Hi = in_Hi[no_mp[x][y]];
                        int Ai = in_Ai[no_mp[x][y]];
                        int Hp = f[sta][r];
                        int Ap = in_Ap;
                        if(r_ * Ap >= Hi) {
                            int nr = r_ - (Hi + Ap - 1) / Ap;
                            int nsta = (sta | getSta(x, y));
                            if(mp[x][y] == 'S') nr = 5;
                            f[nsta][nr] = max(f[nsta][nr], f[sta][r]);
                        } else {
                            int nr = 0;
                            int nsta = sta | getSta(x, y);
                            int Hi_ = Hi - r_ * Ap;
                            int Hp_ = Hp - (Hi_ + Ap - 1) / Ap * Ai;
                            if(mp[x][y] == 'S') nr = 5;
                            f[nsta][nr] = max(f[nsta][nr], Hp_);
                        }
                    }
                }
            }
        }
    }
    int res = 0;
    for(int i = 0; i <= 5; i++) res = max(res, f[key - 1][i]);
    if(res == 0) printf("DEAD\n");
    else printf("%d\n", res);
    return 0;
}







