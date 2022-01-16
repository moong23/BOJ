/*
week 4 data structure(2)
http://acmicpc.net/problem/9012
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ps_check(char *);

int main()
{
    int num;
    char arr[50];
    scanf("%d", &num);
    while (num--)
    {
        scanf("%s", arr);

        if (ps_check(arr) == 1)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        };
    }
    return 0;
}

int ps_check(char arr[50])
{
    int cnt = 0;
    for (int i = 0; i < strlen(arr); i++)
    {
        arr[i] == '(' ? cnt++ : cnt--;
        if (cnt < 0)
            return 0;
    }
    return cnt == 0 ? 1 : 0;
}