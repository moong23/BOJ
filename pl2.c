#include <stdio.h>

int a[10][10][10];

enum days { Sun,
            Mon,
            Tue,
            Wed,
            Thu,
            Fri,
            Sat } d1;

union date {
    char month;
    int day;
    float time;
} d2;

struct department {
    char name[10];
    int dept_id;
    float avg_salary;
} dep;

int *cc, k;

main() {
    k = a[4][5][7];
    d1 = Sun;
    d2.day = k;
    cc = &d2.day;
}