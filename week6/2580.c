/*
week 6 backtracking(2)
http://acmicpc.net/problem/2580
*/

#include <stdio.h>
int N = 0;
int sudoku[9][9];
int mark[81][2];

int backtracking(int k)
{
    if (k == N)
        return 1;

    int X = mark[k][0];
    int Y = mark[k][1];
    int sx = X / 3 * 3;
    int sy = Y / 3 * 3;
    int check[10] = {
        0,
    };
    int result = 0;

    // 가로&세로 체크
    for (int i = 0; i < 9; i++)
        check[sudoku[X][i]] = check[sudoku[i][Y]] = 1;

    // 3x3 사각형 체크
    for (int i = sx; i < sx + 3; i++)
        for (int j = sy; j < sy + 3; j++)
            check[sudoku[i][j]] = 1;

    for (int i = 1; i <= 9; i++)
    {
        if (check[i] == 0)
        {
            sudoku[X][Y] = i;
            result = backtracking(k + 1);
            if (result == 1)
                break;
            sudoku[X][Y] = 0;
        }
    }
    return result;
}

int main()
{
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            scanf("%d", &sudoku[i][j]);
            if (sudoku[i][j] == 0)
            {
                mark[N][0] = i;
                mark[N][1] = j;
                N++;
            }
        }
    }

    backtracking(0);

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
            printf("%d ", sudoku[i][j]);
        puts("");
    }
}