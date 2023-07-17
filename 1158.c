#include <stdio.h>
int main()
{

    int num, k, arr[5000], cnt = -1;
    int ans[5000] = {
        0,
    };
    scanf("%d %d", &num, &k);

    for (int i = 0; i < num; i++)
    {
        arr[i] = i + 1;
    } // array setting from 1
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < k; j++)
        {
            cnt++;
            if (cnt >= num)
            {
                cnt = 0;
            }
            while (arr[cnt] == 0) // 중복된거 찾을때까지
            {
                cnt++;
                if (cnt >= num)
                    cnt = 0;
            }
        }

        ans[i] = arr[cnt];
        arr[cnt] = 0;
    }
    printf("<");
    for (int i = 0; i < num - 1; i++)
    {
        printf("%d, ", ans[i]);
    }
    printf("%d>", ans[num - 1]);
}