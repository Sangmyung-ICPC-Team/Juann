#include <stdio.h>
#include <stdlib.h>

int promising(int i, int col[])
{
	int k = 1;
	while(k < i)
	{
		if(col[i] == col[k] || abs(col[i] - col[k]) == (i - k))
			return 0;
		k++;
	}	

	return 1;
}

int cnt = 0;
void n_queen(int i, int col[], int size)
{
	if(promising(i, col))
	{
		if(i == size)
		{
			cnt++;
			return;
		}		
	
		else
		{
			for(int j = 1; j < size + 1; j++)
			{
				col[i + 1] = j;
				n_queen(i + 1, col, size);
			}
		}
	}
}


int main()
{
	int n;
	scanf("%d", &n);

	int *col = (int*)malloc(sizeof(int) * (n + 1));
	for(int i = 0; i < n + 1; i++)
		col[i] = 0;	

	n_queen(0, col, n);

	printf("%d", cnt);
	return 0;
}
