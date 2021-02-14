n = int(input())

triangle = []

#입력 값 할당
for i in range(n):
    value = []
    value = list(map(int, input().split()))
    triangle.append(value)

#dp table 생성
dp = []

#table 채우기
for i, arr in enumerate(triangle):
    #i는 0 ~ len(triangle)
    #arr은 각 triangle의 원소
    dp.append([]) #list append
    #첫 번째 경우는 따로 빼준다
    if i == 0:
        dp[i].append(arr[0])
        continue
    #First (자신의 위(R) dp table의 값과 자신의 값을 더하여 채움)
    dp[i].append(dp[i - 1][0] + arr[0])
    #Middle (First와 Last를 구분하여서 1 ~ len(arr) - 1까지 반복)
    for j in range(1, len(arr) - 1):
        #왼쪽과 오른쪽에서 오는 경우 중 큰 수를 택하여 채움
        dp[i].append(max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[j])
    #Last (자신의 위(L) dp table의 값과 자신의 값을 더하여 채움)
    dp[i].append(dp[i - 1][len(arr) - 2] + arr[len(arr) - 1])

#마지막 dp table에서 최대값을 출력
print(max(dp[len(triangle) - 1]))
