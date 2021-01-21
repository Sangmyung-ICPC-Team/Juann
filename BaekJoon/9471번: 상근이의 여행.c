#include <stdio.h>
#include <stdlib.h>
#define SIZE 10005

int visited[SIZE] = {0};
int V;

typedef struct GraphNode {
    int vertex;
    struct GraphNode *link;
} GraphNode;

typedef struct GraphType {
    int n;
    GraphNode *adj_list[SIZE];
} GraphType;

void init(GraphType *g)
{
    g->n = 0;
    for(int v = 0; v < SIZE; v++)
    {
        g->adj_list[v] = NULL;
        visited[v] = 0;
    }
}

void insert_vertex(GraphType *g, int num)
{
    g->n = num;
}

void insert_edge(GraphType *g, int u, int v)
{
    GraphNode *node = (GraphNode*)malloc(sizeof(GraphNode));
    node->vertex = v;
    node->link = g->adj_list[u];
    g->adj_list[u] = node;
}

void DFS(GraphType *g, int v)
{
    visited[v] = 1;
    V++;
    for(GraphNode *node = g->adj_list[v]; node; node = node->link)
    {
        if(!visited[node->vertex])
        {
            DFS(g, node->vertex);
        }
    }
}

int main(int argc, const char * argv[]) {
    
    int TC; //Test Case
    scanf("%d", &TC);
    
    GraphType *g = (GraphType*)malloc(sizeof(GraphType));
    init(g);
    
    int N, M; //국가의 수, 비행기의 수
    int u, v; //연결될 두 정점
    for(int i = 0; i < TC; i++)
    {
        scanf("%d%d", &N, &M);
        V = 0;
        insert_vertex(g, N);
        for(int j = 0; j < M; j++)
        {
            scanf("%d%d", &u, &v);
            insert_edge(g, u - 1, v - 1);
        }
        ///
        DFS(g, 0);
        for(int k = 0; k < N; k++)
        {
            if(!visited[k])
                DFS(g, k);
        }
        printf("%d\n", V - 1);
        init(g);
    }
    
    return 0;
}

