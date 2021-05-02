#include <stdio.h>
#include <stdlib.h>

int main()
{
    int k, n;
    int *inarr;
    scanf("%d %d", &k, &n);
    inarr = (int*)malloc(n*sizeof(int));
    for(int i=0;i<n;i++){
        scanf("%d" ,&inarr[i]);
    }

    for(int j=0;j<n;j++){
        
    }

    return 0;
}