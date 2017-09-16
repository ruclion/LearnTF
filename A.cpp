#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int P, Q, N;

double calcu(int start, int add){
    double res = 0;
    double pre = 1.0;
    int now = start;
    for(int i = 0; ; i++) {
        if(now >= 100) {
            res += pre * 1.0;
            break;
        }
        res += pre * 1.0;
        pre = pre * (1 - now / 100.0);
        now += add;
    }
    return res;
}

int main(){
    scanf("%d%d%d", &P, &Q, &N);
    double ans = 0;
    if(N >= 8) {
        ans = (N - 7) * calcu(0, Q);
        N = 7;
    }
    for(int i = 1; i <= N; i++){
        int have = i - 1;
        ans += calcu(P / (int)(pow(2, have) + 0.1), Q);
    }
    printf("%.2f\n", ans);
    return 0;
}
