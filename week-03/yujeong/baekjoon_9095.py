import sys
input = sys.stdin.readline

def DP(n):
    dp = []
    for i in range(n + 1):
        dp.append(0)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    
    for j in range(3, n+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    return dp[n]

T = int(input())
nums = [int(input()) for _ in range(T)]

for num in nums:
    print(DP(num))