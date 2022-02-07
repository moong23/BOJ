/*
https://www.acmicpc.net/problem/18111
*/

#include <stdio.h>
int arr[500][500];

int main()
{
    int n, m, block, avg, min = 64000001, max = 0, min_time, min_block, tmp_time = 0, tmp_block;
    double total = 0;
    scanf("%d %d %d", &n, &m, &block);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &arr[i][j]);
            // total += arr[i][j];
            if (arr[i][j] > max)
                max = arr[i][j];
            if (arr[i][j] < min)
                min = arr[i][j];
        }
    }
    total /= n * m;
    /*
    printf("%lf\n", total);
    if ((int)(total * 10) % 10 >= 0.5)
    {
        avg = (int)total + 1;
    }
    else
    {
        avg = (int)total;
    }
    printf("%d\n", avg);
    */

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            tmp_time += 2 * (arr[i][j] - min);
        }
    }
    min_time = tmp_time;
    min_block = min;
    // printf("%d", min_time);

    for (int idx = min + 1; idx <= max; idx++)
    {
        tmp_block = block;
        tmp_time = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (idx < arr[i][j]) // case 1
                {
                    tmp_time += 2 * (arr[i][j] - idx);
                    tmp_block += (arr[i][j] - idx);
                }
                else // case 2
                {
                    tmp_time += 1 * (idx - arr[i][j]);
                    tmp_block -= (idx - arr[i][j]);
                }
            }
        }
        if (tmp_block < 0)
        {
            // puts("here");
            continue;
        }
        if (min_time == tmp_time)
        {
            min_block = idx;
        }
        if (min_time > tmp_time)
        {
            min_time = tmp_time;
            min_block = idx;
        }
    }
    printf("%d %d\n", min_time, min_block);
    return 0;
}