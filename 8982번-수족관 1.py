num = int(input())

location = []
for _ in range(num):
    x, y = map(int, input().split())
    location.append((x, y))

num = int(input())

hole = []
for _ in range(num):
    x1, y1, x2, y2 = map(int, input().split())
    hole.append([x1, y1, x2, y2])

cnt = 0
change_x = change_y = 0 
x = y = 0

for h in hole:
    for loc in location:
        if loc[0] == 0 and loc[1] == 0:
            continue
        if change_x > loc[0]:
            continue
        #before loction
        #hole보다 아래있는 경우
        max_y = max(h[1], h[3])
        if loc[1] > max_y:
            cnt += (loc[0] - x) * (loc[1] - max_y)
            print("(", loc[0], loc[1], ")", cnt)
        elif loc[1] == max_y:
            x, y = loc[0], loc[1]
            #if (loc[0] == h[0] or loc[0] == h[2]) and (loc[1] == h[1] or loc[1] == h[3]):
                #break
            continue
        else:
            change_x, change_y = loc[0], loc[1]
            x, y = loc[0], loc[1]
            break
        x, y = loc[0], loc[1]

print(cnt)