/*
https://www.acmicpc.net/problem/1550
*/

#include <stdio.h>
#include <string.h>

int main()
{
    int a, len, res = 0;
    char arr[6];
    scanf("%s", arr);
    len = strlen(arr);
    // printf("%d", len);

    for (int i = 0; i < len; i++)
    {
        // printf("%d ", arr[i] - '0');
        if (arr[i] - '0' > 16)
        {
            arr[i] = arr[i] - '0' - 7;
            // printf("%d\n", arr[i]);
        }
        else
        {
            arr[i] -= '0';
        }
        res *= 16;
        res += arr[i];
        // printf("res: %d\n", res);
    }
    printf("%d\n", res);
    return 0;
}