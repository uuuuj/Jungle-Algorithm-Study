# https://www.acmicpc.net/problem/15486

import sys

input = sys.stdin.readline

N = int(input())  # 총 일 수
T = [0] * (N + 1)  # 각 날짜별 상담 기간
P = [0] * (N + 1)  # 각 날짜별 상담 수익

# 입력 처리
for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

# dp[i]: i일에 얻을 수 있는 최대 수익
dp = [0] * (N + 2)  # N+1일까지 접근 가능하도록 +2로 생성

for i in range(1, N + 1):
    # 이전 날까지의 최댓값을 유지
    dp[i] = max(dp[i], dp[i - 1])
    
    # 현재 상담을 했을 때 종료 날짜가 퇴사일(N)을 넘지 않는다면
    if i + T[i] <= N + 1:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

# 최대 수익 출력
print(max(dp))

