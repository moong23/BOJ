/*
week 5 fundamental math(1)
http://acmicpc.net/problem/9663
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int whereQ[15]; // whereQ[a]==b is row:a, column:b
int solutionCnt = 0;
int isValid(int, int, int);
void backtracking(int row, int N) // startN ~ N
{
    if (row > N)
        solutionCnt++;
    else
    {
        for (int i = 1; i <= N; i++)
        {
            if (isValid(row, i, N) == 1)
            {
                whereQ[row] = i;
                backtracking(row + 1, N);
                whereQ[row] = 0;
            }
        }
    }
}
int isValid(int row, int column, int N)
{
    for (int i = 1; i < row; i++)
    {
        if (column == whereQ[i] || abs(row - i) == abs(column - whereQ[i]))
            return 0;
    }
    return 1;
}
int main()
{

    int N;
    scanf("%d", &N);
    backtracking(1, N);
    printf("%d", solutionCnt);
    return 0;
}