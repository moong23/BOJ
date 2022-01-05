#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int N;
    scanf("%d", &N);
    int max = 0, min = 0, bs = 0, mbs = 0;

    int *arr;
    arr = (int *)malloc(sizeof(int) * N);

    for (int i = 0; i < N; i++)
    {
        scanf("%d", arr + i);
        *(arr + i) > max ? max = *(arr + i) : *(arr + i) < min ? min = *(arr + i)
                                                               : min; // min, max
        if (max - min >= 3)
        {
            mbs < bs ? mbs = bs : mbs;
        }
        else
        {
            bs++;
        }
    }

    return 0;
}