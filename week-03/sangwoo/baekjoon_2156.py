# 백준 2156번: 포도주 시식
# https://www.acmicpc.net/problem/2156

import sys

input = sys.stdin.readline

# 포도주 잔의 수
N = int(input())

# 인덱스 1부터 시작하기 위해 앞에 0 추가
wine = [0] + [int(input()) for _ in range(N)]

# dp[i]: i번째 잔까지 고려했을 때 마실 수 있는 최대 포도주 양
dp = [0] * (N + 1)

# 1번째 잔까지 마신 경우
dp[1] = wine[1]

for i in range(2, N + 1):
    if i == 2:
        # 2잔 연속 마실 수 있으므로 둘 다 마심
        dp[2] = wine[1] + wine[2]
        continue

    if i == 3:
        # 연속 3잔은 불가능하므로 가능한 3가지 경우 중 최대값 선택
        dp[3] = max(
            wine[1] + wine[2],  # 1, 2번 마심
            wine[2] + wine[3],  # 2, 3번 마심
            wine[1] + wine[3]   # 1, 3번 마심
        )
        continue

    # i번째까지의 최대값은 다음 중 하나
    dp[i] = max(
        dp[i - 1],                             # 현재 잔을 마시지 않음
        dp[i - 2] + wine[i],                  # 이전 잔을 건너뛰고 현재 잔을 마심
        dp[i - 3] + wine[i - 1] + wine[i]     # 직전 2잔을 마신 형태 (i-2번째는 건너뜀)
    )

# 최종적으로 N번째 잔까지 고려한 최대 마신 양 출력
print(dp[-1])