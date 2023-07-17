/*
week 7 fundamental math(2)
www.acmicpc.net/problem/2485
*/

#include <stdio.h>
#include <stdlib.h>

int arr[100000];
int brr[100000];

int ans(int *, int);
int lcd(int, int);

int main() {
    int num, res;
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 1; i < num; i++) {
        brr[i - 1] = abs(arr[i] - arr[i - 1]);
    }  // initialize brr

    // for (int i = 0; i < num - 1; i++)
    // {
    //     printf("%d ", brr[i]);
    // }
    // puts("");

    res = ans(brr, num - 1);

    printf("%d\n", res);
    return 0;
}

int ans(int brr[], int n) {
    int tmp, res = 0;
    tmp = brr[0] > brr[1] ? lcd(brr[0], brr[1]) : lcd(brr[1], brr[0]);

    // printf("first tmp: %d\n", tmp);
    for (int i = 2; i < n; i++) {
        if (tmp > brr[i])
            tmp = lcd(tmp, brr[i]);
        else
            tmp = lcd(brr[i], tmp);
        // printf("tmp: %d\n", tmp);
    }

    for (int i = 0; i < n; i++) {
        // res += tmp / brr[i];
        res += brr[i] / tmp - 1;
    }
    return res;
}

int lcd(int a, int b) {
    int tmp = -1, tmp_a, tmp_b;
    // printf("%d / %d\n", a, b);
    if (a % b == 0) {
        if (a > b)
            return b;
        else
            return a;
    }
    tmp_a = a;
    tmp_b = b;
    while (tmp != 0) {
        tmp = tmp_a % tmp_b;
        tmp_a = tmp_b;
        tmp_b = tmp;
    }
    // printf("%d\n", tmp_a);
    // printf("%d\n", a * b / tmp_a);
    return tmp_a;
}