/*
https://www.acmicpc.net/problem/5622
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[15];
    int sum = 0;
    scanf("%s", str);
    for (int i = 0; i < strlen(str); i++)
    {
        sum += (str[i] - 'A') / 3 + 2;
        // printf("%c: %d\n", str[i], (str[i] - 'A') / 3 + 2);
    }
    sum += strlen(str);
    printf("%d\n", sum);
    return 0;
}