# https://www.acmicpc.net/problem/17271

import sys

input = sys.stdin.readline

# N: 목표 칸, M: B 스킬의 점프 길이
N, M = map(int, input().split())

# dp[i]: i칸에 도달하는 경우의 수
dp = [0] * (N + 1)

# 초기화: 1칸은 A 버튼 한 번으로만 도달 가능
dp[1] += 1

# 초기화: M칸은 B 버튼 한 번으로만 도달 가능 (M이 N보다 작을 경우에만)
if M <= N:
    dp[M] += 1

# 점화식 적용
# i칸에 도달하는 방법 = i-1칸에서 A 버튼 누르기 + i-M칸에서 B 버튼 누르기
for i in range(2, N + 1):
    if i <= M:
        # 아직 B 버튼을 쓸 수 없는 구간
        dp[i] += dp[i - 1]
    else:
        # B 버튼을 사용할 수 있는 구간
        dp[i] += dp[i - 1] + dp[i - M]

# 정답 출력 (문제에서 요구하는 1,000,000,007으로 나눔)
print(dp[N] % 1_000_000_007)