#include <iostream>
using namespace std;

bool checkDecimal(int x)
{
    if(x == 1)
        return false;

	for(int i = 2; i <= x/2; i++)
	{
		if(x % i == 0)
			return false;
	}
	return true;
}

int main()
{
	int N; cin >> N;
	int *arr = (int*)malloc(sizeof(int) * N);
	int count = 0;

	for(int i = 0; i < N; i++)
	{
		cin >> arr[i];
		if(checkDecimal(arr[i]))
			count += 1;
	}

	cout << count << endl;
	return 0;
}
