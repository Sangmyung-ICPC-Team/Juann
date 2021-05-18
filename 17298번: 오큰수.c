#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 1000000

typedef struct StackType
{
    int data[MAX_STACK_SIZE];
    int top; //스택의 최상단 index = 원소의 개수
} StackType;

void init_stack(StackType *s)
{
    s->top = -1;
}

int is_empty(StackType *s)
{
    if(s->top == -1)
        return 1;
    return 0;
}

int is_full(StackType *s)
{
    if(s->top == (MAX_STACK_SIZE - 1))
        return 1;
    return 0;
}

void push(StackType *s, int value)
{
    if(is_full(s))
        exit(1);
    s->data[++(s->top)] = value;
}

int pop(StackType *s)
{
    if(is_empty(s))
        exit(1);
    return s->data[(s->top)--];
}

int peek(StackType *s)
{
    if(is_empty(s))
        return -1;
    return s->data[s->top];
}

int main()
{
    int N;
    scanf("%d", &N);

    StackType s;
    init_stack(&s);

    int *arr = (int*)malloc(sizeof(int) * N);
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
        push(&s, arr[i]);
    }

    StackType tmp;
    init_stack(&tmp);

    StackType result;
    init_stack(&result);

    ///stack_tmp가 is empty -> print(-1)
    ///stack_tmp에서 s의 top보다 큰 수가 나올 때까지 pop()
    for(int i = N - 1; i >= 0; i--)
    {
        while(!is_empty(&tmp) && peek(&tmp) <= arr[i])
            pop(&tmp);

        if(is_empty(&tmp))
        {
            push(&result, -1);
        }
        else
        {
            push(&result, peek(&tmp));
        }
        push(&tmp, arr[i]);
    }

    while(!is_empty(&result))
        printf("%d ", pop(&result));

    return 0;
}
