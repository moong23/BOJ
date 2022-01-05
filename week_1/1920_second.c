/*
week 1 binary search
http://acmicpc.net/problem/1920

====> using counting sort
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX_INPUT 100000
int arr[MAX_INPUT] = {
    0,
};

int main()
{
    int in, out, value;
    scanf("%d", &in);
    for (int i = 0; i < in; i++)
    {
        scanf("%d", &value);
        arr[value]++;
    }
    scanf("%d", &out);
    for (int j = 0; j < out; j++)
    {
        scanf("%d", &value);
        if (arr[value] > 0)
        {
            printf("1\n");
            arr[value]--;
        }
        else
        {
            printf("0\n");
        }
    }
    return 0;
}