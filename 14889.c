/*
week 6 backtracking(2)
http://acmicpc.net/problem/14889
*/

#include <stdio.h>

int arr[20][20];
int visit[20];
void check(int, int);

int num, min = 200;

int main()
{
    int res;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    } // initialize

    for (int i = 0; i < num; i++)
    {
        visit[i] = 1; // i를 탐색하기로 함
        check(i, 1);
        visit[i] = 0; // i 탐색 끝
    }
    printf("%d\n", min);
}
void check(int idx, int tree)
{
    if (tree == num / 2)
    { // binary tree structure
        int sum1 = 0, sum2 = 0, tmp = 0;
        for (int i = 0; i < num; i++)
        {
            for (int j = 0; j < num; j++)
            {
                if (visit[i] == 1 && visit[j] == 1) // chosen one
                    sum1 += arr[i][j];
                else if (visit[i] == 0 && visit[j] == 0)
                    sum2 += arr[i][j];
            }
        }
        tmp = sum1 > sum2 ? sum1 - sum2 : sum2 - sum1;
        // printf("%d\n", tmp);
        if (min > tmp)
            min = tmp;
        return;
    }
    for (int i = idx + 1; i < num; i++)
    {
        visit[i] = 1;
        check(i, tree + 1);
        visit[i] = 0;
    }
    return;
}