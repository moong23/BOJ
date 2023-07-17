/*
https://www.acmicpc.net/problem/2475
*/

#include <stdio.h>

int main()
{
    int tmp, res = 0;
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &tmp);
        tmp *= tmp;
        res += tmp;
    }
    res %= 10;
    printf("%d\n", res);
    return 0;
}