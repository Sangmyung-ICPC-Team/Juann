#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stack>

using namespace std;
#define SIZE 100001
int main()
{
	stack<char> s;
	
	char string[SIZE];
	scanf("%s", string);

	int len = strlen(string);
	int sum = 0;

	char tmp = string[0]; //memorize before stage 
	s.push(tmp);

	for (int i = 1; i < len; i++)
	{
		if (tmp == '(' && string[i] == ')')
		{
			s.pop();
			sum += s.size();
		}
		else if (string[i] == '(')
			s.push('(');
		else if (string[i] == ')')
		{
			s.pop();
			sum++;
		}
		tmp = string[i];
	}

	printf("%d", sum);

	return 0;
}
