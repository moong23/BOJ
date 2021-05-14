/*
week 2 data structure
http://acmicpc.net/problem/10828
*/

#include <stdio.h>
#include <stdlib.h>

int stack[10000];
int top = -1;

int empty(){
    if(top<0) return 1;
    else return 0;
}

int topnum(){
    if(top<0) return -1;
    else return stack[top];
}

int size(){
    return (top + 1);
}

void push(int value){
    stack[++top] = value;
    return;
}

int pop(){
    if(top<0) return -1;
    else return stack[top--];
}

int main(){
    int num, i = 0, target;
    scanf("%d", &num);
    char str[10];
    while(num--){
        scanf("%s", str);
        if(str[0] == 'p'){
            if(str[1] == 'u'){
                scanf("%d", &target);
                push(target);
            } else {
            printf("%d\n", pop());
            }
        }
        else if(str[0] == 's'){
            printf("%d\n", size());
        }
        else if(str[0] == 'e'){
            printf("%d\n", empty());
        }
        else {
            printf("%d\n", topnum());
        }
    }
}