/*
week 3 search and sort(2)
http://acmicpc.net/problem/11650
*/

#include <stdio.h>
#include <stdlib.h>

// int cmp(const void *, const void *);
void merge(int[], int, int, int);
void mergeSort(int[], int, int);

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
        } // x에 대한 정렬 끝
        // qsort(&b[idx - cnt], cnt, sizeof(int), cmp); // y에 대한 정렬
        mergeSort(&b[idx - cnt], 0, cnt - 1);
    }
    for (int i = 0; i < num; i++)
    {
        printf("%d %d\n", a[i], b[i]);
    }
    return 0;
}

// int cmp(const void *a, const void *b)
// {
//     return *(int *)a - *(int *)b;
// }

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    /* create temp arrays */
    int L[n1], R[n2];

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of L[], if there
    are any */
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there
    are any */
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the
sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l + (r - l) / 2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}