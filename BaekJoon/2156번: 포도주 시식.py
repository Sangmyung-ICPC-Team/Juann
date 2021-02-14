n = int(input())

bottle = []
for i in range(n):
    value = int(input())
    bottle.append(value)
def grape():
    if n == 1:
        return bottle[0]
    dp = []
    dp.append(0) #0
    dp.append(bottle[0]) #1
    dp.append(bottle[0] + bottle[1]) #2

    for i in range(3, n + 1):
        value = max(bottle[i - 2] + dp[i - 3], dp[i - 2]) + bottle[i - 1]
        if value < dp[i - 1]:
            value = dp[i - 1]
        dp.append(value)
    return dp[n]

print(grape())
