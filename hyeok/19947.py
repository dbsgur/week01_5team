import sys

input = sys.stdin.readline

# H원 Y년
H, Y = map(int, input().split())

max_value = 0


def getMaxProfit(money, year):
    dp = [0 for i in range(year+1)]
    dp[0] = money
    for i in range(1, Y+1):
        dp[i] = int(dp[i-1]*1.05)
        if i >= 3:
            dp[i] = max(int(dp[i-3]*1.2), dp[i])
        if i >= 5:
            dp[i] = max(int(dp[i-5]*1.35), dp[i])
    return dp[year]


print(getMaxProfit(H, Y))
