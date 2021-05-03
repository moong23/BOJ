/*
https://www.acmicpc.net/problem/3572
*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int h, w, n;
    int *arr, *board;

    scanf("%d %d %d", &h, &w, &n);
    arr = (int *)calloc(n, sizeof(int));
    board = (int *)calloc(h, sizeof(int));

    for(int i=0;i<h;i++){
        board[i] += w;
    }

    for(int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }

    int foundflag;
//arr[i] => 안내판의 길이
//board[j] => j행의 남은 길이
    for (int i=0; i<n; i++){
        foundflag = 0;
        for(int j=0; j<h; j++){ // 게시판 한줄씩 확인
            if(arr[i] <= board[j]){ // 들어갈 자리 있으면!
                board[j] -= arr[i];
                printf("%d\n", j+1);
                foundflag = 1;
                break;
            }
        }
        if(foundflag == 0){
            printf("-1\n");
        }
    }

    free(arr);
    free(board);

    return 0;
}