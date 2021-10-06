#include <iostream>
#include <algorithm>

int main()
{
	int n; scanf("%d", &n);
	int *arr = (int*)malloc(sizeof(int) * (n+1));

	arr[0] = 0;
	arr[1] = 1;
	arr[2] = 2;

	for(int i = 3; i <= n; i++)
	{
		arr[i] = (arr[i-1] + arr[i-2]) % 10007;
	}

	printf("%d", arr[n]);

	return 0;
}
