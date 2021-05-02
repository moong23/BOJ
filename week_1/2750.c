#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
#define MAX_SIZE 1000000    //데이터의 개수 지정
#define SWAP(x,y,t) ((t)=(x), (x)=(y), (y)=(t))    //SWAP함수 설정
int original[MAX_SIZE];    //랜덤함수로 만든 데이터를 저장할 원본 배열
int list_a[MAX_SIZE];    //각 정렬 알고리즘에서 사용할 데이터 배열
int list_b[MAX_SIZE];    //각 정렬 알고리즘에서 사용할 데이터 배열
int list_c[MAX_SIZE];    //각 정렬 알고리즘에서 사용할 데이터 배열
int n; //데이터의 개수를 받는 전역변수 설정
int sorted[MAX_SIZE]; //합병정렬에서 사용할 데이터를 저장할 배열
clock_t start, finish, used_time=0;    //실행 시간 측정을 위한 변수

//quick sort 
int partition(int list[], int left, int right)
{
    int pivot=list[left], tmp, low=left, high=right+1;
 
    do{
        do
        low++;
        while(low<=right && list[low]<pivot);
 
        do
        high--;
        while(high>=left && list[high]>pivot);
        if(low<high) SWAP(list[low], list[high], tmp);
    }while(low<high);
 
    SWAP(list[left], list[high], tmp);
    return high;
}
void quick_sort(int list[], int left, int right)
{
    if(left<right)
    {
        int q=partition(list, left, right);
        quick_sort(list, left, q-1);
        quick_sort(list, q+1, right);
    }
}

//선택 정렬
void selection_sort(int list[], int n)
{
    int i,j,least,tmp;
    
    for(i=0; i<n-1; i++)
    {
        least=i;
        for(j=i+1; j<n; j++)
            if(list[j]<list[least]) least=j;
        SWAP(list[i], list[least], tmp);
    }
}

void CopyArr_a(void)
{
    int i;
    for(i=0; i<n; i++)
        list_a[i]=original[i];
}

void CopyArr_b(void)
{
    int i;
    for(i=0; i<n; i++)
        list_b[i]=original[i];
}
 
 void CopyArr_c(void)
{
    int i;
    for(i=0; i<n; i++)
        list_c[i]=original[i];
}
 
 
//실행 시간을 측정 및 출력하는 함수
void CalcTime(void)
{
    used_time=finish-start;
    printf("완료!\n소요 시간 : %f sec\n\n",(float)used_time/CLOCKS_PER_SEC);
}

int cmp(const void* a, const void* b){
    return *(int*)a > *(int*)b ? 1: *(int*)a < *(int*)b ? -1 : 0;
}


int main()
{
    int i;
    n = MAX_SIZE;
    for(i=0;i<n;i++){
        original[i] = rand();
    }

    printf("데이터의 개수 : %d\n\n", n);
   
    //selection sort
    CopyArr_a();
    start = clock();
    printf("selection sort... " );
    selection_sort(list_a, n);
    finish = clock();
    CalcTime();

    //quick sort
    CopyArr_b();
    start = clock();
    printf("quick sort... " );
    quick_sort(list_b, 0, n);
    finish = clock();
    CalcTime();

    //qsort
    CopyArr_c();
    start = clock();
    printf("qsort... " );
    qsort(list_c, n, sizeof(int), cmp);
    finish = clock();
    CalcTime();

    return 0;
}