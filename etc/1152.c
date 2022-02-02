/*
https://www.acmicpc.net/problem/1152
*/
#include <stdio.h>
#include <string.h>
char arr[1000001];
int main()
{
    int leng, cnt = 0;
    scanf("%[^\n]", arr);
    leng = strlen(arr);
    // for (int i = 0; i < leng; i++)
    //     printf("%c", arr[i]);
    if (arr[0] == ' ')
        cnt--;
    for (int i = 0; i < leng; i++)
    {
        if (arr[i] == ' ' && arr[i + 1] != ' ')
            cnt++;
    }
    if (arr[leng - 1] == ' ')
        cnt--;
    printf("%d\n", cnt + 1);
    return 0;
}