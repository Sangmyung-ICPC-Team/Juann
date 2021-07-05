from collections import deque

def get_answer(N, arr):
    d = deque()
    arr.sort()

    for i, value in enumerate(arr):
        if i % 2== 0:
            d.append(value)
        else:
            d.appendleft(value)

    m = -1
    for i in range(len(d) - 1):
        temp = abs(d[i] - d[i + 1])
        if m < temp:
            m = temp

    temp = abs(d[0] - d[len(arr) - 1])
    if m < temp:
        m = temp

    print(m)

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    get_answer(N, arr)
