/*
https://www.acmicpc.net/problem/15829
*/

#include <stdio.h>
#include <math.h>
#define M 1234567891

int main()
{
    int leng;
    long long int hash = 0, R = 1;
    char arr[50], tmp;
    scanf("%d ", &leng);

    for (int i = 0; i < leng; i++)
    {
        // scanf("%c", &arr[i]);
        scanf("%c", &tmp);
        hash = (hash + (tmp - 'a' + 1) * R) % M;
        R = (R * 31) % M;
        // printf("%d/ %d: %lf / %lf\n", i, tmp - 'a' + 1, pow(31, i), (tmp - 'a') * pow(31, i));
    }
    printf("%lld\n", hash);
    return 0;
}