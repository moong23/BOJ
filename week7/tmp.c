/*
week 7 fundamental math(2)
www.acmicpc.net/problem/6588
*/

#include <stdio.h>

int isPrime(int);

int main()
{
    int num = -1;
    while (1)
    {
        scanf("%d", &num);
        if (num == 0)
            break;
        for (int i = 3; i <= num / 2; i += 2)
        {
            if (isPrime(i) == 1)
            {
                if (isPrime(num - i) == 1)
                {
                    printf("%d = %d + %d\n", num, i, num - i);
                    break;
                }
                else
                {
                    continue;
                }
            }
            else
            {
                continue;
            }
        }
    }
    return 0;
}

int isPrime(int i)
{
    // printf("checking %d\n", i);
    int res = 1;

    for (int j = 3; j <= i / 2; j += 2)
    {
        if (i / j != 1 && i % j == 0) // not prime number
        {
            return 0;
        }
    }
    // printf("%d is prime number\n", i);
    return res;
}