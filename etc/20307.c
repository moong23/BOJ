/*
https://www.acmicpc.net/problem/20307
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int row, col;
    scanf("%d %d", &row, &col);
    //memory allocation
    int **arr;
    arr = (int **)malloc(sizeof(int *) * row);
    for (int i = 0; i < row; i++)
    {
        arr[i] = (int *)malloc(sizeof(int) * col);
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf("%d", arr[i][j]);
        }
        puts("");
    }

    //free memory
    for (int i = 0; i < row; i++)
    {
        free(arr[i]);
    }
    free(arr);

출처:
https: //codeng.tistory.com/8 [도전!]
    return 0;
}