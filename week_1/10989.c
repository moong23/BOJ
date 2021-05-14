/*
week 1 binary search
http://acmicpc.net/problem/10989
*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, max, min, num;
    int *arr;
    arr = (int*)calloc(10001, sizeof(int)); //들어오는 수의 범위 : 1 ~ 10000 but 편의를 위해 10001만큼 할당
    max = 1, min = 10000;
    scanf("%d", &n);
    for(int i=0;i<n;i++){
        scanf("%d", &num);
        arr[num]++;
        max < num ? max = num : max;
        min > num ? min = num : min;
    }
    for(int i=min; i<=max; i++){
        if (arr[i]>0){
            for(int j=0;j<arr[i];j++){
                printf("%d\n", i);
            }
        }
    }
    return 0;
}