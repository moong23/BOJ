#include <stdio.h>
#include <stdlib.h>

int main()
{
	int cse, i, num, j, sum, cnt = 0, k;
	float avg;
	int* arr;
	scanf("%d", &cse);
	arr = (int*)malloc(sizeof(int));
	for (i = 0; i < cse; i++)
	{
		sum = 0, cnt = 0;
		scanf("%d", &num);
		arr = (int*)realloc(arr, num * sizeof(int));
		for (j = 0; j < num; j++)
		{
			scanf("%d", &arr[j]);
			sum += arr[j];
		}
		avg = (float)(sum) / (float)num;
		for (k = 0; k < num; k++)
		{
			if (arr[k] > avg)
				cnt++;
		}
		printf("%.3f%%\n", 100*(float)((float)cnt / (float)num));
	}

	return 0;
}