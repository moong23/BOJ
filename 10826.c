/*
https://www.acmicpc.net/problem/10826
*/

#include <stdio.h>
int num;
long long int arr[10001] = {
    0,
    1,
    1,
};
void fib(int);

int main()
{
    scanf("%d", &num);
    if (num > 2)
        fib(num);

    /*
    for (int i = 0; i <= num; i++)
    {
        printf("%d ", arr[i]);
    }
    puts("");
    */
    printf("%lld\n", arr[num]);
    return 0;
}

void fib(int num)
{
    for (int i = 3; i <= num; i++)
    {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    return;
}