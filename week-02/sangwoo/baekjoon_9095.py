# https://www.acmicpc.net/problem/9095

import sys

input = sys.stdin.readline

N = int(input())

nums = [ int(input()) for _ in range(N) ]

max_n = max(nums)

dp = [ 0 ] * (max_n + 1)

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(1, max_n):
  if i + 1 <= max_n: dp[i + 1] += dp[i]
  if i + 2 <= max_n: dp[i + 2] += dp[i]
  if i + 3 <= max_n: dp[i + 3] += dp[i]


for n in nums:
  print(dp[n])