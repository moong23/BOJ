/*
https://www.acmicpc.net/problem/1259
*/

#include <stdio.h>
#include <string.h>

int main()
{
    int num, tmp, leng, flag;
    char arr[100000];
    while (1)
    {
        flag = 1;
        leng = 0;
        scanf("%d", &num);
        if (num == 0)
            break;
        tmp = num;
        while (tmp != 0)
        {
            arr[leng] = tmp % 10 + '0';
            tmp /= 10;
            leng++;
        }
        // for (int i = 0; i < leng; i++)
        // {
        //     printf("%c", arr[i]);
        // }
        // puts("");
        for (int i = 0; i <= leng / 2; i++)
        {
            if (arr[i] != arr[leng - 1 - i])
            {
                flag *= -1;
                break;
            }
        }
        flag == 1 ? printf("yes\n") : printf("no\n");
    }
    return 0;
}