#include <iostream>
using namespace std;

int getSum(int num, int *dp)
{
    if (num < 3)
        return num;
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i = 4; i <= num; i++)
    {
        for(int j = i-1; j >= i-3; j--)
            dp[i] += dp[j];
    }
    return dp[num];
}

int main()
{
    int testCase; scanf("%d", &testCase);
    
    int num;
    int *dp;
    for(int i = 0; i < testCase; i++)
    {
        scanf("%d", &num);
        dp = (int*)malloc(sizeof(int) * (num+1));
        printf("%d\n", getSum(num, dp));
    }
    return 0;
}
