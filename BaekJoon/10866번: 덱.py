import sys
from collections import deque

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    d = deque()
    
    for _ in range(N):
        command = list(map(str, sys.stdin.readline().split()))

        if command[0] == "push_front":
            d.appendleft(command[1])
        
        if command[0] == "push_back":
            d.append(command[1])

        if command[0] == "pop_front":
            if len(d):
                print(d.popleft())
            else:
                print(-1)
        if command[0] == "pop_back":
            if len(d):
                print(d.pop())
            else:
                print(-1)
        if command[0] == "size":
            print(len(d))

        if command[0] == "empty":
            if len(d):
                print(0)
            else:
                print(1)
        if command[0] == "front":
            if len(d):
                print(d[0])
            else:
                print(-1)
        if command[0] == "back":
            if len(d):
                temp = d.pop()
                print(temp)
                d.append(temp)
            else:
                print(-1)                
