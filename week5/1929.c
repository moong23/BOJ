/*
week 5 fundamental math(1)
http://acmicpc.net/problem/1929
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int a, b;
    int arr[1000000];
    clock_t t_s, t_e;

    scanf("%d %d", &a, &b);

    t_s = clock();
    //algorithm start
    for (int i = a; i <= b; i++)
    {
        arr[i] = 1;
    } // initialize
    arr[1] = 0;

    for (int i = 2; i < b; i++)
    {
        int tmp = b / i;
        for (int j = 2; j <= tmp; j++)
        {
            arr[i * j] = 0;
        }
    }

    t_e = clock();
    for (int i = 1; i <= b; i++)
    {
        if (arr[i] == 1)
            printf("%d\n", i);
    }
    printf("running time: %lf\n", (double)(t_e - t_s) / CLOCKS_PER_SEC);
    return 0;
}