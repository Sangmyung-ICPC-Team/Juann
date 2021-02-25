from collections import deque

N, K = map(int, input().split())

def breath_first_search():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        #가능한 경우의 수를 모두 돌아본다
        for step in (v - 1, v + 1, v * 2):
            #step이 정규 범위 안에 속하면서 방문하지 않은 곳이라면 
            if 0 <= step < MAX and not time[step]:
                #현재 vertex의 time에 + 1을 하여 update한다.
                time[step] = time[v] + 1
                #현재 vertex를 queue에 넣는다.
                q.append(step)

MAX = 100001 
time = [0] * MAX #Min time table
breath_first_search()

