#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STACK_SIZE 100

typedef struct StackType {
	char stack[MAX_STACK_SIZE];
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

void push(StackType *s, char value)
{
	if(is_full(s))
		exit(1);
	s->stack[++(s->top)] = value;
}

char pop(StackType *s)
{
	if(is_empty(s))
		exit(1);
	return s->stack[(s->top)--];
}

char peek(StackType *s)
{
	return s->stack[s->top];
}

int prec(char op)
{
	switch(op)
	{
		case '(': case ')':
			return 0;
		case '+': case'-':
			return 1;
		case '*': case '/':
			return 2;
	}
	return -1;
}

char postfix[MAX_STACK_SIZE];

void infix_top_postfix(char exp[])
{
	int index = 0;

	StackType s;
	init_stack(&s);

	char ch, top_op;
	int len = strlen(exp);

	for(int i = 0; i < len; i++)
	{
		ch = exp[i];
		switch(ch)
		{
			case '+': case '-': case '*': case '/':
				while(!is_empty(&s) && (prec(ch) <= prec(peek(&s))))
					postfix[index++] = pop(&s);
				push(&s, ch);
				break;
			case '(':
				push(&s, ch);
				break;
			case ')':
				top_op = pop(&s);
				while(top_op != '(')
				{
					postfix[index++] = top_op;
					top_op = pop(&s);
				}
				break;
			default:
				postfix[index++] = ch;
				break;
		}
	}
	while(!is_empty(&s))
		postfix[index++] = pop(&s);
}

int main()
{
	char exp[MAX_STACK_SIZE];
	scanf("%s", exp);

	infix_top_postfix(exp);
	printf("%s", postfix);

	return 0;
}
