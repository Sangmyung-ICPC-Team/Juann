#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 1000001

typedef struct QueueType {
	int data[MAX_QUEUE_SIZE];
	int front, rear;
} QueueType;

void init_queue(QueueType *q)
{
	q->front = -1;
	q->rear = -1;
}

int is_full(QueueType *q)
{
	if(q->rear == (MAX_QUEUE_SIZE - 1))
			return 1;
	return 0;
}

int is_empty(QueueType *q)
{
	if(q->front == q->rear)
		return 1;
	return 0;
}

void enqueue(QueueType *q, int value)
{
	if(is_full(q))
		exit(1);
	q->data[++(q->rear)] = value;
}

int dequeue(QueueType *q)
{
	if(is_empty(q))
		exit(1);
	return q->data[++(q->front)];
}

int main()
{
	int num;
	scanf("%d", &num);

	QueueType q;
	init_queue(&q);

	for(int i = 0; i < num; i++)
		enqueue(&q, i + 1);

	int tmp1, tmp2;
	while(!is_empty(&q))
	{
		tmp1 = dequeue(&q);
		if(is_empty(&q))
			break;
		tmp2 = dequeue(&q);
		
		enqueue(&q, tmp2);
	}
	printf("%d", tmp1);
	
	return 0;
}
