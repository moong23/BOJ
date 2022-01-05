/*
week 3 search and sort(2)
http://acmicpc.net/problem/11650
*/

#include <stdio.h>
#include <stdlib.h>

int cmp(const void *, const void *);

int main()
{
    int num, min = 100000, max = -100000, idx = 0, cnt = 1;
    int *x, *y, *a, *b;

    scanf("%d", &num);
    x = (int *)malloc(sizeof(int) * num);
    y = (int *)malloc(sizeof(int) * num);
    a = (int *)malloc(sizeof(int) * num);
    b = (int *)malloc(sizeof(int) * num);

    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &x[i], &y[i]);
        min = min < x[i] ? min : x[i];
        max = max > x[i] ? max : x[i];
    }

    for (int i = min; i <= max; i++)
    {
        cnt = 0;
        for (int j = 0; j < num; j++)
        {
            if (i == x[j])
            {
                a[idx] = x[j];
                b[idx] = y[j];
                idx++;
                cnt++;
            }
        }                                            // x에 대한 정렬 끝
        qsort(&b[idx - cnt], cnt, sizeof(int), cmp); // y에 대한 정렬
    }
    for (int i = 0; i < num; i++)
    {
        printf("%d %d\n", a[i], b[i]);
    }
    return 0;
}

int cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}