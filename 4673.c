/*
https://www.acmicpc.net/problem/4673
*/

#include <stdio.h>

int self(int);

int main()
{
    printf("1\n3\n5\n7\n9\n20\n31\n42\n53\n64\n75\n86\n97\n");
    for (int i = 101; i <= 10000; i++)
    {
        if (!self(i))
            printf("%d\n", i);
    }
    return 0;
}

int self(int num)
{
    int res = 0;
    for (int i = 80; i < num; i++)
    {
        int tmp = i, leng = 0;
        while (tmp != 0)
        {
            tmp /= 10;
            leng++;
        }
        tmp = i;
        res = i;
        for (int j = 0; j < leng; j++)
        {
            res += tmp % 10;
            tmp /= 10;
        }
        if (res == num)
        {
            return 1;
        }
    }
    return 0;
}