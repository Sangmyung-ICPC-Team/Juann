#include <iostream>
#include <stack>

using namespace std;

int main()
{
	int N; scanf("%d", &N);

	int cnt = 0;
	
	stack<pair<int, int >> s;
	pair<int, int> p; //index, value

	int input;

	while (cnt < N)
	{
		scanf("%d", &input);
		p = make_pair(cnt + 1, input);

		while (!s.empty())
		{
			if (s.top().second > input)
			{
				printf("%d ", s.top().first);
				break;
			}
			s.pop();
		}

		if (s.empty())
			printf("0 ");

		s.push(p);
		cnt++;
	}

	return 0;
}
