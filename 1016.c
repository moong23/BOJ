/*
week 7 fundamental math(2)
www.acmicpc.net/problem/1016
*/

#include <stdio.h>
int cnt = 0;
void check(long long int);
int main()
{
    long long int min, max;
    scanf("%lld %lld", &min, &max);

    for (long long int i = min; i <= max; i++)
    {
        check(i);
    }
    printf("%d\n", max - min - cnt + 1);
    return 0;
}
void check(long long int i)
{
    for (long long int j = 2; j * j <= i; j++)
    {
        if (i % (j * j) == 0)
        {
            cnt++;
            // printf("%d\n", i);
            break;
        }
    }
    return;
}