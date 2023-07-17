/*
https://www.acmicpc.net/problem/1002
*/

#include <math.h>
#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);
    while (num--) {
        int xa, xb, ya, yb, ra, rb;
        float d;
        scanf("%d %d %d %d %d %d", &xa, &ya, &xb, &yb, &ra, &rb);
        d = pow((xa - xb), 2) + pow((ya - yb), 2);
        d = sqrt(d);
        printf("***%d %d %d %f\n", ra, rb, ra + rb, d);
        if (d == 0 && ra == rb)
            puts("-1");
        else if (d < ra + rb)
            puts("0");
        else if (d == (float)(ra + rb))
            puts("1");
        else if (d > ra + rb)
            puts("2");
    }
    return 0;
}