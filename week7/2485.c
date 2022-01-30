/*
week 7 fundamental math(2)
www.acmicpc.net/problem/2485
*/

#include <stdio.h>
#include <stdlib.h>

int arr[100000];
int brr[100000];

int ans(int *, int);
int lcd(int, int);

int main()
{
    int num, res;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &arr[i]);
    }

    for (int i = 1; i < num; i++)
    {
        brr[i - 1] = abs(arr[i] - arr[i - 1]);
    } // initialize brr

    for (int i = 0; i < num - 1; i++)
    {
        printf("%d ", brr[i]);
    }
    puts("");

    res = ans(brr, num - 1);

    printf("%d\n", res);
    return 0;
}

int ans(int brr[], int n)
{
    int tmp;
    tmp = brr[0] > brr[1] ? lcd(brr[0], brr[1]) : lcd(brr[1], brr[0]);
    printf("first tmp: %d\n", tmp);
    for (int i = 2; i < n; i++)
    {
        gcd(tmp, brr[i]);
    }

    return tmp;
}

int lcd(int a, int b)
{
    printf("%d / %d : %d\n", a, b, a % b);
    if (a % b == 0)
    {
        return b;
    }
    else
    {
        lcd(b, a % b);
    }
}