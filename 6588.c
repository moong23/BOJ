/*
week 7 fundamental math(2)
www.acmicpc.net/problem/6588
*/

#include <stdio.h>
#define MAX_INPUT 1000000 // max input 1000000
// int isPrime(int);
void PrimeTable();

int Prime[MAX_INPUT];
/*
    value = 0 : prime
    value = 1 : not prime
*/

int main()
{
    int num;
    PrimeTable();
    while (1)
    {
        scanf("%d", &num);
        if (num == 0)
            break;
        for (int i = 3; i <= num / 2; i += 2)
        {
            if (Prime[i] == 0 && Prime[num - i] == 0)
            {
                printf("%d = %d + %d\n", num, i, num - i);
                break;
            }
        }
        /*for (int i = 3; i < num / 2; i+= 2)
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
        }*/
    }
    return 0;
}
/* // testcase가 들어올 때마다 check하니까 시간 초과가 나온다
int isPrime(int i)
{
    // printf("checking %d\n", i);
    int res = 1;
    for (int j = 2; j <= i / 2; j++)
    {
        if (i / j != 1 && i % j == 0) // not prime number
        {
            res = 0;
            // printf("%d is not prime number\n", i);
            return res;
        }
    }
    // printf("%d is prime number\n", i);
    return res;
}*/

void PrimeTable()
{
    for (int i = 2; i <= MAX_INPUT; i++)
    {
        for (int j = 2; Prime[i] == 0 && i * j < MAX_INPUT; j++)
        {
            Prime[i * j] = 1;
        }
    }
    return;
}