/*
https://www.acmicpc.net/problem/8370
*/

#include <stdio.h>

int main()
{
    int a, b, res = 0;
    scanf("%d %d", &a, &b);
    res = a * b;
    scanf("%d %d", &a, &b);
    res += a * b;
    printf("%d\n", res);
    return 0;
}