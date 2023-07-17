#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N;
        scanf("%d", &N);
        int **arr;
        arr = (int **)malloc(sizeof(int *) * N);
        for (int i = 0; i < N; i++) {
            arr[i] = (int *)malloc(sizeof(int) * N);
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                scanf("%d", &arr[i][j]);
            }
        }
        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < N; j++) {
        //         printf("%d ", arr[i][j]);
        //     }
        //     printf("\n");
        // }

        int cnt = 0;
    }

    return 0;
}