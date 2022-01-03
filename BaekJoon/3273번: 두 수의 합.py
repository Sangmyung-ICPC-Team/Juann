#Standard Input
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

#pointer
p1, p2 = 0, n - 1

res = 0
#p1 -> mid <- p2
while p1 < p2:
    if arr[p1] + arr[p2] == x:
        res += 1
        p1 += 1
        p2 -= 1
    elif arr[p1] + arr[p2] < x:
        p1 += 1
    else:
        p2 -= 1
print(res)
