/*
week 1 binary search
http://acmicpc.net/problem/1920
*/

#include <stdio.h>
#include <stdlib.h>

void swap(int*, int*);
int cmp(const void*, const void*);

int main(){
    
    int m, n, i, j, min, min_n;
    int * arr, * brr;

    scanf("%d", &m);
    arr = (int*)malloc(m * sizeof(int));
    
    for(i=0;i<m;i++){
        scanf("%d", arr+i);
    }

    //------------------------------- 내장 정렬 함수
    qsort(arr,m,sizeof(int),cmp);

    // puts("-----");
    // for(i=0;i<m;i++){
    //     printf("%d", *(arr+i));
    // }
    // puts("");


/*
    //arr배열 오름차순 정렬 using selection sort
    for(i = 0 ; i < m ; i++){
        min = *(arr+i);
        min_n = i;
        for(j = i ; j < m ; j++){
            if(min > *(arr+j)){
                min = *(arr+j);
                min_n = j;
            }
        }
        swap(arr+i, arr+min_n);
    }
*/
    //search할 num 배열 brr input
    scanf("%d", &n);
    brr = (int*)malloc(n * sizeof(int));

    i = 0;

    while(i < n){
        scanf("%d", brr+i);
        i++;
    }

    //brr => arr Binary Search
    int left, right, mid, flag;

    for(i = 0;i<n;i++){//brr 하나씩 체크!
        flag = 0;
        left = 0, right = m-1; // 초기세팅
        if(*(arr) == *(brr+i) || *(arr+m-1) == *(brr+i)){
            flag = 1;
        }
        while(flag == 0){
            mid = (left + right)/2;
            if(left == mid || right == mid) {
                break;
            }
            if(*(arr+mid) == *(brr+i)){
                flag = 1;
                break;
            }
            
            if(*(arr+mid) > *(brr+i)){
                right = mid;
            } else {
                left = mid;
            }
            

        }
        printf("%d\n", flag);
    }

    return 0;
}

void swap(int* a, int* b){
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
    return;
}

int cmp(const void* a, const void* b){
    return *(int*)a > *(int*)b ? 1: *(int*)a < *(int*)b ? -1 : 0;
}
