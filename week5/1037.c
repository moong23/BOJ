/*
week 5 fundamental math(1)
http://acmicpc.net/problem/2609
*/
/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int num, res = 1;
    double tmp, ans;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &tmp);
        res *= tmp;
    }
     ==> num이 짝수일 때
        약수의 곱 = (답)^(약수의 개수 / 2)
        (res * ans) = (ans)^((num+2)/2)
        res = (ans)^(num/2)
        ans = res^(2/num)
    
// tmp = pow((num) / 2, -1);

// printf("%lf\n", tmp);
// ans = pow(res, tmp);
// ans = kthRoot(res, num / 2);
// ans = pow(res, 2);
ans = pow(res, 1 / 3);
printf("%d", (int)ans);
return 0;
}
* /
*/

#include <stdio.h>
#include <stdlib.h>
int cmp(const void *, const void *);

int main()
{
    int num;
    int arr[50];
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d", arr + i);
    }
    qsort(arr, num, sizeof(int), cmp);
    // printf("%d %d\n", arr[0], arr[num - 1]);
    printf("%d\n", arr[0] * arr[num - 1]);
    return 0;
}
int cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}