from collections import deque

def slicing(S):
    arr = []
    for i in range(6):
        arr.append(S[i + 1])
    return arr

while True:
    S = deque(map(int, input().split()))

    result = []
    for i in range(len(S) - 1):
        for j in range(len(S)): #복원까지 + 1
                arr = slicing(S)
                arr.sort() #정렬
                if arr not in result:
                    result.append(arr)
                temp1, temp2 = S.popleft(), S.popleft() #임시
                S.rotate(-1) #회전
                #복원
                S.appendleft(temp2)
                S.appendleft(temp1)
        temp1, temp2 = S.popleft(), S.popleft() #임시
        S.appendleft(temp1)
        S.append(temp2)
    
    result.sort()
    for i in result:
        for j in i:
            print(j, end=' ')
        print('\n')
