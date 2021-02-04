#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char * argv[]) {
    int n; scanf("%d", &n);
    
    int *dp = (int*)malloc(sizeof(int) * (n + 1));
    dp[0] = 0; dp[1] = 1; dp[2] = 2;
    
    for(int i = 3; i <= n; i++)
    {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
    }
    
    printf("%d", dp[n]);
    
    return 0;
}
