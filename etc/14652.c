/*
http://acmicpc.net/problem/14652
*/

#include <stdio.h>

int main()
{
    int n, m, k;

    scanf("%d %d %d", &n, &m, &k);

    int res_n, res_m;
    res_n = k / m;
    res_m = k % m;

    printf("%d %d\n", res_n, res_m);
    return 0;
}