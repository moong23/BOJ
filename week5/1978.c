/*
week 5 fundamental math(1)
http://acmicpc.net/problem/1978
*/

#include <stdio.h>

int is_Prime(int);

int main()
{
    int num, cnt = 0, tmp;
    scanf("%d", &num);
    while (num--)
    {
        scanf("%d", &tmp);
        if (is_Prime(tmp) == 1)
            cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}

int is_Prime(int num)
{
    int i;
    if (num == 1)
        return 0;
    if (num == 2)
        return 1;
    for (i = 2; i < num; i++)
    {
        if (num % i == 0)
            return 0;
    }
    return 1;
}