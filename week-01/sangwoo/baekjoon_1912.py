# https://www.acmicpc.net/problem/1912

import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

dp = [0] * N              # dp[i]: i번째까지의 부분 수열 중 최대 합
dp[0] = nums[0]           # 첫 번째 수는 그대로 시작

for i in range(1, N):
    # 현재 수만 단독으로 시작할 것인가 vs 이전 수열에 이어붙일 것인가
    dp[i] = max(nums[i], nums[i] + dp[i - 1])

print(max(dp))            # 전체 중 최댓값 출력