/*
https://www.acmicpc.net/problem/2798
*/

#include <stdio.h>

int arr[100];

int main()
{
    int N, M, sum, max = 0;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            for (int k = j + 1; k < N; k++)
            {
                sum = arr[i] + arr[j] + arr[k];
                if (sum <= M)
                    max = max < sum ? sum : max;
            }
        }
    }
    printf("%d\n", max);
    return 0;
}