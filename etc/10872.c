/*
https://www.acmicpc.net/problem/10872
*/
#include <stdio.h>
int main()
{
    int num;
    scanf("%d", &num);
    int res = 1;
    for (int i = 1; i <= num; i++)
    {
        res *= i;
    }
    printf("%d\n", res);
    return 0;
}