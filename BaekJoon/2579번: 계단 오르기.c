#include <stdio.h>
#include <stdlib.h>

int max(int a, int b)
{
    return a >= b ? a : b;
}

int upstairs(int *arr, int n)
{
    int *dp = (int*)malloc(sizeof(int) * (n + 1));
    if(n == 1)
        return arr[0];
    if(n == 2)
        return arr[0] + arr[1];
    
    dp[0] = 0;
    dp[1] = arr[0];
    dp[2] = arr[1] + arr[0];
    for(int i = 3; i <= n; i++)
    {
        dp[i] = max(dp[i - 3] + arr[i - 2], dp[i - 2]) + arr[i - 1];
    }
    return dp[n];
}

int main(int argc, const char * argv[]) {
    int n; //계단의 개수
    scanf("%d", &n);
    
    int *arr = (int*)malloc(sizeof(int) * n);
    
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    
    printf("%d", upstairs(arr, n));
    
    return 0;
}

