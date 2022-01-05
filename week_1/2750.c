/*
week 1 binary search
http://acmicpc.net/problem/2750
*/

#include <stdio.h>
#include <stdlib.h>

int cmp(const void *, const void *);

int main()
{
    int n, *arr;
    scanf("%d", &n);

    arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        scanf("%d", arr + i);
    }

    qsort(arr, n, sizeof(int), cmp);

    for (int i = 0; i < n; i++)
    {
        printf("%d\n", *(arr + i));
    }

    return 0;
}

int cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}