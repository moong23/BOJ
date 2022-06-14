/*
week 4 data structure(2)
http://acmicpc.net/problem/1874
*/

#include <stdio.h>

int flag = 1; // available status
int t_cnt = 0;
void func(int);
void push(int);
int arr[100000];
char ans[300000];
int main()
{
    int num, tmp;
    scanf("%d", &num);
    while (num--)
    {
        scanf("%d", &tmp);
        func(tmp);
    }
    if (flag)
    {
        for (int i = 0; i < t_cnt; i++)
        {
            printf("%c", ans[i]);
        }
    }
    else
    {
        printf("NO\n");
    }
}

int max = 0;

void func(int tmp)
{
    if (tmp > max)
    {
        push(tmp);
        max = tmp;
    }
}
void push(int tmp)
{
    for (int i = max; i < tmp; i++)
    {
        ans[i] = '+';
        t_cnt++;
    }
}