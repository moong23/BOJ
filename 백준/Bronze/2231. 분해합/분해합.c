/*
https://www.acmicpc.net/problem/2231
*/

#include <stdio.h>
int res = 0, num;
int check(int);
int main()
{

    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        if (check(i) == 1)
        {
            res = i;
            break;
        }
    }

    printf("%d\n", res);
}
int check(int i)
{
    int tmp = i, len = 0, cal;
    while (tmp)
    {
        tmp /= 10;
        len++;
    }

    tmp = i;
    cal = tmp;
    for (int i = 0; i < len; i++)
    {
        cal += tmp % 10;
        tmp /= 10;
    }
    if (cal == num)
        return 1;
    else
        return 0;
}