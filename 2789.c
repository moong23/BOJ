/*
https://www.acmicpc.net/problem/2789
*/

#include <stdio.h>
#include <string.h>
int main()
{
    char str[100];
    scanf("%s", str);
    for (int i = 0; i < strlen(str); i++)
    {
        if (str[i] != 'C' && str[i] != 'A' && str[i] != 'M' && str[i] != 'B' && str[i] != 'R' && str[i] != 'I' && str[i] != 'D' && str[i] != 'G' && str[i] != 'E')
        {
            printf("%c", str[i]);
        }
    }
    puts("");
    return 0;
}