#include <stdio.h>
#include <stdlib.h>

int cmp (const void*, const void*);

int main(){
    int num;
    scanf("%d", &num);
    int *arr;
    arr = (int*)malloc(num*sizeof(int));
    for(int i=0;i<num;i++){
        scanf("%d", arr+i);
    }

    qsort(arr, num, sizeof(int), cmp);

    long long int cnt = 0, tmp;
    for(int i=0;i<num;i++){
        tmp = arr[i] - i;
        if(tmp >= 0){
            cnt += tmp;
        } else {
            cnt -= tmp;
        }
    }
    

    printf("%lld", cnt);
    return 0;
}

int cmp (const void* a, const void*b){
    return *(int*)a - *(int*)b;
}