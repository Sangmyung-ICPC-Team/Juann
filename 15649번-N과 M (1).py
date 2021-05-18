N, M = map(int, input().split()) # M: depth
result = []
visited = [False] * (N + 1) # 숫자가 1부터 시작하기 때문에 index 1부터 사용

def depth_first_search(depth, N, M):
    if depth == M + 1: # 최대 출력 개수 
        for i in range(len(result)):
            print(result[i], end=' ') #공백으로 분리하여 출력
        print() #한 줄에 하나씩
        return
    for num in range(1, N + 1): # 1 ~ (N+1)
        if not visited[num]: #방문하지 않은 경우
            visited[num] = True #방문처리 
            result.append(num)
            #다음 수를 찾으러 recursion 
            depth_first_search(depth + 1, N, M)
            #init
            visited[num] = False
            result.pop()
# 1부터 시작
depth_first_search(1, N, M)