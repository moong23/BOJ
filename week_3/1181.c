/*
week 3 search and sort(2)
http://acmicpc.net/problem/1181
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int num;
    char arr[20000][50]; // [개수][길이]
    char brr[20000][50];
    char ans[20000][50];
    int leng[20000], cnt = 0, cnt_same = 0;

    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%s", arr[i]);
    }

    // *** sort ascending order by length
    // first, give leng_array arr's string's length.
    for (int i = 0; i < num; i++)
    {
        leng[i] = strlen(arr[i]);
    }

    //sorting starts here
    for (int i = 1; i < 50; i++, cnt_same = 0)
    {
        for (int j = 0; j < num; j++)
        {
            if (leng[j] == i)
            {
                if (cnt_same != 0)
                { // if there's multiple same length string
                    for (int k = 1; k < cnt_same; k++)
                    {
                        if (strcmp(brr[cnt - k], arr[i]) > 0) // strcmp returns negative integer if string is in ascending order.
                        {
                            char tmp[50];
                            strcpy(tmp, brr[cnt - k]);
                            strcpy(brr[cnt - k], arr[i]);
                            strcpy(arr[i], tmp);
                        }
                    }
                }
                else
                {
                    strcpy(brr[cnt++], arr[i]);
                }
                cnt_same++;
            } // if there's same length string, sort by alphabetical ascending order.
        }
    }

    //test
    for (int i = 0; i < num; i++)
    {
        // printf("%d\n", leng[i]);
        printf("%s\n", brr[i]);
    }

    return 0;
}
/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sort(int *leng, char **p)
{
    char temp[51];
    int temp2;

    for (int i = 0; leng[i] != 0; i++) //using bubble sort
    {
        for (int j = 0; leng[j] != 0; j++)
        {
            if ((leng[j] > leng[j + 1]) && leng[j + 1] != 0)
            {
                //leng_array swap
                temp2 = leng[j];
                leng[j] = leng[j + 1];
                leng[j + 1] = temp2;

                //p_array swap
                strcpy(temp, p[j]);
                strcpy(p[j], p[j + 1]);
                strcpy(p[j + 1], temp);
            }
            else if (leng[j] == leng[j + 1])
            {
                if (strcmp(p[j], p[j + 1]) > 0)
                {
                    strcpy(temp, p[j]);
                    strcpy(p[j], p[j + 1]);
                    strcpy(p[j + 1], temp);
                }
            }
        }
    }
}

int main()
{
    int n;
    int leng[20000] = {
        0,
    };
    scanf("%d", &n);
    char **p;
    p = (char **)malloc(sizeof(char *) * n);
    for (int i = 0; i < n; i++)
    {
        p[i] = (char *)malloc(sizeof(char) * 50);
        scanf("%s", p[i]);
        leng[i] = strlen(p[i]);
    } // p[num][50]
    sort(leng, p);

    for (int i = 0; i < n; i++)
    {
        if ((i != n - 1) && (strcmp(p[i], p[i + 1]) == 0))
        {
            continue;
        }
        printf("%s\n", p[i]);
    }

    return 0;
}
*/