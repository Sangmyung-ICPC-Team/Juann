#include <stdio.h>
#include <stdlib.h>

typedef struct I {
	int start, end; //시작 시간, 종료 시간
	int time; //회의 시간
} I;

int compare(const void *a, const void *b)
{
	I *pa = (I *)a;
	I *pb = (I *)b;

	int a_start = pa->start;
	int b_start = pb->start;

	int a_end = pa->end;
	int b_end = pb->end;

	if(a_end != b_end) 
	{
		if(a_end < b_end) return -1;
		else if(a_end == b_end) return 0;
		else return 1;
	}
	else
	{
		if(a_start < b_start) return -1;
		else if(a_start == b_start) return 0;
		else return 1;
	}
}


int main()
{
	int N; scanf("%d", &N);
	I *conference = (I*)malloc(sizeof(I) * N);

	for(int i = 0; i < N; i++)
	{
		scanf("%d%d", &conference[i].start, &conference[i].end);
		conference[i].time = conference[i].end - conference[i].start;
	}

	qsort(conference, N, sizeof(I), compare);
	
	int cnt = 0; //회의 개수
	int end_time = -1; //회의 종료 시간
	for(int i = 0; i < N; i++)
	{
		if(conference[i].start >= end_time)
		{
			cnt++;
			end_time = conference[i].end;
		}
	}

	printf("%d", cnt);


	return 0;
}
