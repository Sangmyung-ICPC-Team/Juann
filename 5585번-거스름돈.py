pay = int(input())
cost = 1000 - pay

coin = [500, 100, 50, 10, 5, 1]

cnt = 0
while cost > 0:
    for value in coin:
        cnt += cost // value
        cost %= value
print(cnt)