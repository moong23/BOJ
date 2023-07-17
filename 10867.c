/*
week 3 search and sort(2)
http://acmicpc.net/problem/10867
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, val, min = 2000, max = 0;
    int arr[2000] = {
        0,
    }; // will use counting sort
    scanf("%d", &num);
    while (num--)
    {
        scanf("%d", &val);
        val += 1000;
        arr[val]++;
        min = min > val ? val : min;
        max = max < val ? val : max;
    }
    for (int i = min; i <= max; i++)
    {
        if (arr[i] != 0)
        {
            printf("%d ", i - 1000);
        }
    }
    // puts("");
    return 0;
}