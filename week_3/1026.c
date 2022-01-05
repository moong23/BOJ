/*
week 3 search and sort(2)
http://acmicpc.net/problem/1026
*/

#include <stdio.h>
#include <stdlib.h>
// #define MAX_IDX_NUM 50;
int cmp(const void *, const void *);

int main()
{
    /*
    arr의 값을 재배열하여 sum(a[i]*b[i])의 값을 작게만들기
    +) brr은 재배열하면 안됨
    => array에 들어오는 값들이 0이상의 정수이므로 brr의 크기가 큰 순서대로 index값을 알 수 있다면 arr을 그 순서의 역순으로 정렬해주면 될듯?
    */
    int *arr, *brr, *idx;
    int N_arr;
    scanf("%d", &N_arr);

    arr = calloc(N_arr, sizeof(int));
    brr = calloc(N_arr, sizeof(int));
    idx = calloc(N_arr, sizeof(int));

    for (int i = 0; i < N_arr; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < N_arr; i++)
    {
        scanf("%d", &brr[i]);
    }

    int tmp, max, sum = 0;
    qsort(arr, N_arr, sizeof(int), cmp); // arr sort by descending order.

    // for (int i = 0; i < N_arr; i++)
    // {
    //     printf("%d", arr[i]);
    // }
    // puts("");
    for (int i = 0; i < N_arr; i++)
    {
        tmp = 0;
        max = brr[0];
        for (int j = 0; j < N_arr; j++)
        {
            if (brr[j] > max)
            {
                max = brr[j];
                tmp = j;
            }
        } // finding biggest num and it's idx of brr
        sum += max * arr[i];
        brr[tmp] = -1;
        // printf("max : %d, sum : %d\n", max, sum);
    }
    printf("%d\n", sum);
}

int cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}