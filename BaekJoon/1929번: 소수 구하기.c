///에라토스테네스의 체 이용
#include <stdio.h>
#define SIZE 1000005
int none_prime[SIZE] = {0, 1, 0};

int main() {

    int M, N;
    scanf("%d%d", &M, &N);
    
    for(int i = 2; i < SIZE; i++)
    {
        if(!none_prime[i])
        {
            for(int j = 2; j * i < SIZE; j++)
            none_prime[j * i] = 1;
        }
    }
    
    for(int i = M; i <= N; i++)
        if(!none_prime[i])
            printf("%d\n", i);
    
    return 0;
}

