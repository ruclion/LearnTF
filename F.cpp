#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 1e6;
int len[maxn];
int n, N;
char S[maxn], s[maxn], ch[10];
int maxr, p, idx;

void preAndGetLen() {
    for(int i = 1; i <= n; i++){
        S[2 * i - 1] = '#';
        S[2 * i] = s[i];
    }
    S[2 * n + 1] = '#';
    N = 2 * n + 1;
    maxr = -1;
    p = -1;
    len[0] = 0;
    idx = 0;
    for(int i = 1; i <= N; i++) {
        if(maxr < i) {
            len[i] = 1;
        } else {
            len[i] = min(maxr - i + 1, len[2 * p - i]);
        }
        while(i + len[i] <= N && i - len[i] >= 1 && S[i + len[i]] == S[i - len[i]]) {
            len[i]++;
        }
        if(i + len[i] - 1 > maxr) {
            maxr = i + len[i] - 1;
            p = i;
        }
        if(len[i] > len[idx]) idx = i;
    }
}
void out(char t) {
    int no = ((t - 'a' - ch[0] + 'a') % 26 + 26) % 26;
    printf("%c", (char)(no +'a'));
}

int main(){
    while(scanf("%s %s", ch, s + 1) != EOF){
        n = strlen(s + 1);
        preAndGetLen();
        int ans = (2 * len[idx] - 1) / 2;
        if(ans > 1){
            int pp = (idx + 1) / 2;
            if(ans % 2 == 0) {
                printf("%d %d\n", pp - ans / 2 - 1, pp + ans / 2 - 1 - 1);
            } else {
                printf("%d %d\n", pp - ans / 2 - 1, pp + ans / 2 - 1);
            }
            for(int i = idx - len[idx] + 1; i <= idx + len[idx] - 1; i++) {
                if(S[i] != '#') {
                    out(S[i]);
                }
            }
            printf("\n");
        } else {
            printf("No solution!\n");
        }
    }
    return 0;
}
