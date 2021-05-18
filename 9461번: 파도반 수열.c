#include <stdio.h>

long long memo[105] = { 0 };

long long padovan(int N)
{
	if (memo[N])
		return memo[N];
	if (N == 0)
		return 0;
	if ( N == 1 || N == 2)
		return 1;
	return memo[N] = padovan(N - 3) + padovan(N - 2);
}

int main()
{
	int TC;
	scanf("%d", &TC);

	int num;
	for (int i = 0; i < TC; i++)
	{
		scanf("%d", &num);
		printf("%lld\n", padovan(num));
	}

	return 0;
}
