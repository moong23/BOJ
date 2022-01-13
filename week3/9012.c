// #define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
    int cnt, n;
    char s[21];
    char t[1001];

    scanf("%d", &cnt);

    for (int i = 0; i < cnt; i++)
    {
        scanf("%d", &n);
        scanf("%s", s);
        int ch = n;
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                t[j * ch + k] = s[j];
                // printf("n: %d\n s: %s\n t: %s\n", j, s, t);
                // printf("k: %d, n: %d\n", k, n);
            }
        }
        printf("%s\n", s);
        // printf("%c, %d, %d\n", t[9], n, (int)strlen(s));
        t[n * strlen(s)] = '\0';

        printf("%s\n", t);
    }
    return 0;
}