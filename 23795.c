/*
https://www.acmicpc.net/problem/23795
*/

#include <stdio.h>

int main()
{
    int tmp;
    long long int res = 0;
    while (1)
    {
        scanf("%d", &tmp);
        if (tmp == -1)
            break;
        res += tmp;
    }
    printf("%lld\n", res);
    return 0;
}