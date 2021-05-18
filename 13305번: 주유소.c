#include <stdio.h>
#include <stdlib.h>

void input_distance(int *distance, int N)
{
    for(int i = 0; i < N - 1; i++)
    {
        scanf("%d", &distance[i]);
    }
}

void input_cost(int *cost, int N)
{
    for(int i = 0; i < N; i++)
        scanf("%d", &cost[i]);
}

long long get_total(int *distance, int *cost, int N)
{
    long long min = cost[0];
    long long index = 0;
    long long total = 0;

    for(int i = 1; i < N; i++)
    {
        if(min >= cost[i])
        {
            total += (min) * distance[index++];
            min = cost[i];
        }
        else
            total += (min) * distance[index++];
    }
    return total;
}

int main()
{
    int N;
    scanf("%d", &N); //도시의 개수

    int *distance = (int*)malloc(sizeof(int) * (N - 1)); //도시 간의 거리
    input_distance(distance, N);

    int *cost = (int*)malloc(sizeof(int) * N); //주유 비용
    input_cost(cost, N);

    printf("%lld", get_total(distance, cost, N));

    return 0;
}
