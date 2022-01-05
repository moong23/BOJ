/*
week 3 search and sort(2)
http://acmicpc.net/problem/10816
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX_INPUT_SIZE 10000000

int main()
{
    int num, val;
    printf("here111");
    int arr[2 * MAX_INPUT_SIZE] = {
        0,
    }; // will use counting sort
    printf("here");
    scanf("%d", &num);
    while (num--)
    {
        scanf("%d", &val);
        val += MAX_INPUT_SIZE;
        arr[val]++;
    } // input finished

    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &val);
        val += MAX_INPUT_SIZE;
        printf("%d ", arr[val]);
    }

    // puts("");
    return 0;
}