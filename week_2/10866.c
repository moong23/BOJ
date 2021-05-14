/*
week 2 data structure
http://acmicpc.net/problem/10866
*/

#include <stdio.h>
#include <stdlib.h>

int deque[20000];
int front = 10000, rear = 10000;


int empty(){
    if(front == rear) return 1;
    else return 0;
}

void push_front(int value){
    deque[--front] = value;
}

void push_back(int value){
    deque[rear++] = value;
}

int pop_front(){
    if(empty() == 1) return -1;
    else return deque[front++];
}

int pop_back(){
    if(empty() == 1) return -1;
    else return deque[--rear];
}

int size(){
    return rear - front;
}


int frontnum(){
    if(empty() == 1) return -1;
    else return deque[front];
}

int backnum(){
    if(empty() == 1) return -1;
    else return deque[rear-1];
}

int main(){
    int num, value;
    char str[15];
    scanf("%d", &num);
    while(num--){
        scanf("%s", str);
        if(str[0] == 'p'){ //p로 시작
            if(str[5] == 'f'){
                scanf("%d", &value);
                push_front(value);
            } else if(str[5] == 'b'){
                scanf("%d", &value);
                push_back(value);
            } else if(str[4] == 'f'){
                scanf("%d", &value);
                printf("%d\n", pop_front());
            } else {
                scanf("%d", &value);
                printf("%d\n", pop_back());
            }
        } else if(str[0] == 's'){
            printf("%d\n", size());
        } else if(str[0] == 'e'){
            printf("%d\n", empty());
        } else if(str[0] == 'f'){
            printf("%d\n", frontnum());
        } else if(str[0] == 'b'){
            printf("%d\n", backnum());
        }
    }
}