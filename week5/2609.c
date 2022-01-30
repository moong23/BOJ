/*
week 5 fundamental math(1)
http://acmicpc.net/problem/2609
*/

#include <stdio.h>
#include <stdlib.h>

void GCD(int, int);
// int LCM(int, int, int);

int res = 1;

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);

    GCD(a, b);
    // l = LCM(a, b, res);

    printf("%d\n%d\n", res, a * b / res);
    return 0;
}

void GCD(int a, int b)
{
    int min, i;
    min = a < b ? a : b;
    for (i = 2; i <= min; i++)
    {
        if (a % i == 0 && b % i == 0)
        {
            // printf("here!: %d\n", i);
            res *= i;
            break;
        }
    }
    a /= i;
    b /= i;
    if (a == 0 | b == 0)
    {
        return;
    }
    else
    {
        GCD(a, b);
    }
}

// int LCM(int a, int b, int g)
// {
//     int res;
//     res = a * b;
//     res /= g;
//     return res;
// }