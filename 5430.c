/*
week 4 data structure(2)
http://acmicpc.net/problem/5430
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_INPUT_SIZE 100000
char cmd[MAX_INPUT_SIZE];
char arr[3 * MAX_INPUT_SIZE + 2] = {
    ' ',
};
int brr[MAX_INPUT_SIZE] = {
    0,
};
int main()
{
    int cse, num, direction, leng, end, start = 0, cnt = 0, f;
    scanf("%d", &cse);
    while (cse--)
    {
        cnt = 0;
        direction = 0;
        start = 0;
        scanf("%s", cmd);
        scanf("%d", &num); // num <= 100000
        leng = num;
        end = num;
        scanf("%s", arr);
        int tmp = 0;
        for (int i = 0; i < 4 * num + 2; i++) // putting int only into array_b ............. integer overflow?
        {
            if (arr[i] == '[')
                continue;
            else if (arr[i] == ',' | arr[i] == ']')
            {
                brr[cnt++] = tmp;
                tmp = 0;
                continue;
            }
            else
            {
                tmp *= 10;
                tmp += arr[i] - '0';
            }
        }
        f = strlen(cmd);
        for (int i = 0; i < f; i++)
        {
            if (cmd[i] == 'R')
            {
                direction = 1 - direction;
                /* direction is a variable which shows array's direciton
                    direction = 0 : ->
                    direction = 1 : <-
                */
            }
            else if (cmd[i] == 'D')
            {
                if (leng <= 0)
                {
                    printf("error");
                    goto Exit;
                }
                switch (direction)
                {
                case 0: // direction ->
                    start++;
                    leng--;
                    break;
                case 1: // //direction <-
                    end--;
                    leng--;
                    break;
                }
            }
        }
        if (leng == 1)
        {
            printf("[%c]", arr[start]);
        }
        else if (direction == 0)
        {
            printf("[");
            for (int i = start; i < end - 1; i++)
            {
                printf("%d,", brr[i]);
            }
            printf("%d]", brr[end - 1]);
        }
        else if (direction == 1)
        {
            printf("[");
            for (int i = end - 1; i > start; i--)
            {
                printf("%d,", brr[i]);
            }
            printf("%d]", brr[start]);
        }
    Exit:
        puts("");
    }
    return 0;
}