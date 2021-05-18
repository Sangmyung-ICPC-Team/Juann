#include <stdio.h>
#include <stdlib.h>

int main()
{
	int N, K;
	scanf("%d%d", &N, &K);

	int *arr = (int*)malloc(sizeof(int) * N);
	for(int i = 0;i < N; i++)
		scanf("%d", &arr[i]);

	int cnt = 0;
	int index = N - 1;
	int tmp;

	while(K > 0)
	{
		tmp = K / arr[index];
		if(tmp)
		{	
			cnt += K / arr[index];
			K = K % arr[index];
		}
		index--;
	}

	printf("%d", cnt);

	return 0;
}
