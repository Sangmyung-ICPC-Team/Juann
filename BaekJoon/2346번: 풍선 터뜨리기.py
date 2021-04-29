from sys import stdin
from collections import deque

if __name__ == "__main__":
    N = int(stdin.readline())
    q = deque(enumerate(map(int, stdin.readline().split())))
    answer = []

    while True:
        idx, paper = q.popleft()
        answer.append(idx + 1)

        if not q:
            break

        if paper > 0:
            # rotate(-) == append(q.popleft())
            q.rotate(-(paper - 1))
        elif paper < 0:
            # rotate(+) == appendleft(q.pop())
            q.rotate(-paper)

    print(' '.join(map(str, answer)))
