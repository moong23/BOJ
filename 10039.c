/*
https://www.acmicpc.net/problem/10039
*/

#include <stdio.h>

int main()
{
    int a, res = 0;
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &a);
        if (a >= 40)
            res += a;
        else
            res += 40;
    }
    printf("%d\n", res / 5);
    return 0;
}