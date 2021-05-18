#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 100001

typedef struct StackType {
	int data[MAX_STACK_SIZE];
	int top;
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

void push(StackType *s, int item)
{
	if(is_full(s))
		exit(1);
	s->data[++(s->top)] = item;
}

int pop(StackType *s)
{
	return s->data[(s->top)--];
}

int main()
{
	StackType s; 
	init_stack(&s);

	int num; scanf("%d", &num);
	int *arr = (int*)malloc(sizeof(int) * num);

	for(int i = 0; i < num; i++)
	{
		scanf("%d", &arr[i]);
		if(!arr[i])
			pop(&s);
		else
			push(&s, arr[i]);
	}

	int sum = 0;
	while(!is_empty(&s))
	{
		sum += pop(&s);
	}

	printf("%d", sum);

	return 0;
}
