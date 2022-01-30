/*
https://www.acmicpc.net/problem/5554
*/

#include <stdio.h>

int main()
{
    int tmp, res = 0, res_m, res_s;
    for (int i = 0; i < 4; i++)
    {
        scanf("%d", &tmp);
        res += tmp;
    }
    res_m = res / 60;
    res_s = res % 60;
    printf("%d\n%d\n", res_m, res_s);
    return 0;
}