/*
week 2 data structure
http://acmicpc.net/problem/10845
*/

#include <stdio.h>
#include <stdlib.h>

int front = -1, rear = -1;
int queue[10000];

int empty(){
    if(front == rear) return 1;
    else return 0;
}

void push(int value){
    queue[++rear] = value;
}

int pop(){
    if(empty() == 1) return -1;
    else return queue[++front];
}

int size(){
    return rear - front;
}

int frontnum(){
    if(empty() == 1) return -1;
    else return queue[front+1];
}

int backnum(){
    if(empty() == 1) return -1;
    else return queue[rear];
}

int main(){
    int num, target;
    char str[10];
    scanf("%d", &num);
    while(num--){
        scanf("%s", str);
        if(str[0] == 'p'){
            if(str[1] == 'u'){
                scanf("%d", &target);
                push(target);
            } else {
                printf("%d\n", pop());
            }
        } else if(str[0] == 'f'){
            printf("%d\n", frontnum());
        } else if(str[0] == 'b'){
            printf("%d\n", backnum());
        } else if(str[0] == 'e'){
            printf("%d\n", empty());
        } else if(str[0] == 's'){
            printf("%d\n", size());
        }
    }
}