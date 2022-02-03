/*
week 7 fundamental math(2)
www.acmicpc.net/problem/15711
*/

#include <stdio.h>
#define MAX_INPUT 2000000000000

long long int Prime[MAX_INPUT];
/*
    value = 0 : prime
    value = 1 : not prime
*/

void isPrime(long long int);

int main()
{
    int testcse;
    long long int A, B, tmp;
    scanf("%d", &testcse);
    while (testcse--)
    {
        scanf("%lld %lld", &A, &B);
        tmp = A + B;
        if (tmp < 4)
        {
            printf("NO\n");
            continue;
        }
        else if (tmp % 2 == 0)
        {
            printf("YES\n");
            continue;
        }
        isPrime(tmp);
    }
    return 0;
}

void PrimeTable()
{
    for (long long int i = 2; i <= MAX_INPUT; i++)
    {
        for (long long int j = 2; Prime[i] == 0 && i * j < MAX_INPUT; j++)
        {
            Prime[i * j] = 1;
        }
    }
    return;
}

void isPrime(long long int num)
{
    for (long long int i = 3; i < num / 2; i += 2)
    {
        if (!Prime[i] && !Prime[num - i])
        {
            printf("YES\n");
            return;
        }
    }
    printf("NO\n");
    return;
}