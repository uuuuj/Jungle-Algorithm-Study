import sys

input = sys.stdin.readline

# 여러 테스트 케이스 처리
while True:
  # N: 수열의 길이
  N = int(input())

  # N이 0이면 입력 종료
  if N == 0:
    break

  # P: 수열 입력받기
  P = [int(input()) for _ in range(N)]

  # dp[i]: i번째 원소를 마지막으로 포함하는 연속 부분합의 최댓값
  dp = [0 for _ in range(N)] 

  # 첫 번째 원소는 그 자체가 최대 부분합
  dp[0] = P[0]

  # 동적 프로그래밍으로 각 위치의 최대 부분합 계산
  for i in range(1, N):
    # 두 가지 선택:
    # 1. 현재 원소부터 새로 시작: P[i]
    # 2. 이전 부분합에 현재 원소 추가: dp[i-1] + P[i]
    dp[i] = max(P[i], dp[i - 1] + P[i])

  # 모든 위치 중 최댓값이 정답
  print(max(dp))