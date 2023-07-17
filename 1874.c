/*
week 4 data structure(2)
http://acmicpc.net/problem/1874
*/

#include <stdio.h>
#include <stdlib.h>

int stack[200000] = {
    0,
},
    cnt = 0, a_cnt, max = 0;
char ans[100000000] = {
    ' ',
};

void push(int val)
{
    for (int i = max; i < val; i++)
    {
        stack[cnt++] = i;
        ans[a_cnt++] = '+';
    }
    max = max < val ? val : max;
    ans[a_cnt++] = '-';
    stack[cnt--] = 0;
    // printf("cnt: %d\n", cnt);
    return;
}

int pop(int val)
{
    int tmp;
    if (stack[cnt - 1] != val)
        return 0;
    else
    {
        stack[cnt--] = 0;
        ans[a_cnt++] = '-';
    }
    return 1;
}
int do_stack(int val) // stack에 push할지, pop할지, terminate할지 결정
{
    // printf("val: %d stack: %d max: %d\n", val, stack[cnt - 1], max);
    if (val > stack[cnt - 1])
        push(val);
    else
    {
        if (!pop(val))
        {
            return 0; // pop()함수에서 0을 return하면 terminate
        };
    }
    return 1;
}

int main()
{
    int num, val;
    scanf("%d", &num);
    while (num--)
    {
        scanf("%d", &val);

        if (do_stack(val) == 0)
        {
            printf("NO\n");
            return 0;
        }
    }

    {
        for (int i = 0; i < a_cnt; i++)
        {
            printf("%c\n", ans[i]);
        }
    }

    return 0;
}