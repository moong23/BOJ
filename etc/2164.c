/*
https://www.acmicpc.net/problem/2164
*/

#include <stdio.h>

int main()
{
    int num, front = 0, rear;
    int queue[500000];
    scanf("%d", &num);

    for (int i = 0; i < num; i++)
        queue[i] = i + 1;
    rear = num - 1;
    while (1)
    {
        front = (front + 1) % num;
        if (rear == front)
            break;
        rear = (rear + 1) % num;
        queue[rear] = queue[front];
        front = (front + 1) % num;
        if (rear == front)
            break;
    }
    printf("%d\n", queue[rear]);
    return 0;
}