/*
https://www.acmicpc.net/problem/24218
*/

#include <stdio.h>

int main()
{
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);
    float ra, rb, rc, res;
    ra = a * 2 * 0.229 * 0.324;
    rb = b * 2 * 0.297 * 0.420;
    rc = c * 0.210 * 0.297;
    res = ra + rb + rc;
    printf("%lf\n", res);
}