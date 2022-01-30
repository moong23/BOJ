/*
https://www.acmicpc.net/problem/1712
*/

#include <stdio.h>
long long int ans(int, int, int);

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%lld\n", ans(a, b, c));
    return 0;
}
long long int ans(int a, int b, int c)
{
    int res = -1;
    long long int i = 1;
    if (b >= c)
        return res;
    res = a / (c - b) + 1;
    return res;
}