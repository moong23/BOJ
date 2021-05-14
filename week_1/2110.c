#include <stdio.h>
#include <stdlib.h>

int cmp(const void* , const void*);

int main(){
    int n, c;
    scanf("%d %d", &n, &c);

    int *arr = (int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++){
        scanf("%d", arr+i);
    }
    qsort(arr, n, sizeof(int), cmp);

    

    return 0;
}

int cmp(const void* a, const void* b){
    return *(int*)a > *(int*)b ? 1: *(int*)a < *(int*)b ? -1 : 0;
}