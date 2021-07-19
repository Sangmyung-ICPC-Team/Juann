#include <stdio.h>
#include <stdlib.h>

int memo[45] = { 0 };

int fib(int N)
{
	if (memo[N])
		return memo[N];
	if (N == 0)
		return 0;
	if (N == 1)
		return 1;
	return memo[N] = fib(N - 1) + fib(N - 2);
}

int main()
{
	int test_case; scanf("%d", &test_case);

	int N;
	for (int i = 0; i < test_case; i++)
	{
		scanf("%d", &N);
		if (N == 0) printf("1 0\n");
		else if (N == 1) printf("0 1\n");
		else
		{
			printf("%d %d\n", fib(N - 1), fib(N));
		}
	}

	return 0;
}
