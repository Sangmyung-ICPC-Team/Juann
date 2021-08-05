#include <bits/stdc++.h>
using namespace std;

int main()
{
	int N; cin >> N;
	int *arrA, *arrB;
	arrA = (int*)malloc(sizeof(int) * N);
	arrB = (int*)malloc(sizeof(int) * N);

	for(int i = 0; i < N; i++)
		cin >> arrA[i];
	for(int i = 0; i < N; i++)
		cin >> arrB[i];

	sort(arrA, arrA + N); 
	sort(arrB, arrB + N, greater<int>());

	int sum = 0;
	for(int i = 0; i < N; i++)
		sum += arrA[i] * arrB[i];

	cout << sum << endl;

	return 0;
}
