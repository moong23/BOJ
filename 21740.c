#include <stdio.h>
#include <stdlib.h>

int main(){
    int num, usedflag = 0, tmp, maxnum = 0;
    int *arr;
    scanf("%d", &num);
    arr = (int*)calloc(10, sizeof(int));
    for(int i=0;i<num;i++){
        scanf("%d", tmp);
        arr[tmp]++;
    }//input by cntsort => input can be bigger than 10!
    for(int i=0;i<num;i++){
        
    }
    
}