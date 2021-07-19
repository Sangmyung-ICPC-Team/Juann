#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 200002

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
    {
        printf("NO");
        exit(1);
    }
    return s->data[(s->top)--];
}

int main()
{
    int num;
    scanf("%d", &num);
    int *arr = (int*)malloc(sizeof(int) * MAX_STACK_SIZE);
    int *tmp = (int*)malloc(sizeof(int) * MAX_STACK_SIZE);

    StackType s;
    init_stack(&s);

    for(int i = 0; i < num; i++)
    {
        scanf("%d", &arr[i]);
        tmp[i] = i + 1;
    }


    int index = 0; //tmp_index
    int x, y;
    x = y = 0;

    char *string = (char*)malloc(sizeof(char) * MAX_STACK_SIZE);
    int s_index = 0;

    for(int i = 0; i < num; i++) //arr_index
    {
        x = arr[i];
        if(x > y)
        {
            do
            {
                if(index >= num)
                {
                    printf("NO");
                    return 0;
                }
                string[s_index++] = '+';
                push(&s, tmp[index]);
            }
            while(tmp[index++] != arr[i]);
            pop(&s);
            string[s_index++] = '-';
        }
        else
        {
            pop(&s);
            string[s_index++] = '-';
        }

        y = x;
    }

    if(is_empty(&s))
        for(int i = 0; i < s_index; i++)
            printf("%c\n", string[i]);
    else
        printf("NO");

    return 0;
}
