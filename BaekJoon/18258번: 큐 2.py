from collections import deque
import sys

N = int(sys.stdin.readline())

queue = deque()

def excute(temp):
    if temp[0] == "push":
        queue.append(temp[1])
    elif temp[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif temp[0] == "size":
        print(len(queue))
    elif temp[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif temp[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif temp[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            a = queue.pop()
            print(a)
            queue.append(a)



for _ in range(N):
    temp = []
    temp = sys.stdin.readline().split()
    excute(temp)
