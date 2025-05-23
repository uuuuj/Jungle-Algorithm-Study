# 백준 18405번: 경쟁적 전염
# https://www.acmicpc.net/problem/18405

import heapq
import sys

input = sys.stdin.readline

# N: 시험관 크기, K: 바이러스 종류 수
N, K = map(int, input().split())

# 방향 벡터 (우, 하, 좌, 상)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = []           # (시간, 바이러스 번호, y, x) 형식으로 우선순위 큐에 저장
board = []       # 시험관 상태

# 시험관 초기 상태 입력
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] != 0:
            # 바이러스가 존재하면 큐에 넣음 (초기 시간 0)
            heapq.heappush(q, (0, row[j], i, j))
    board.append(row)

# S: 경과 시간, X, Y: 출력할 위치
S, X, Y = map(int, input().split())

# BFS + 우선순위 큐를 이용한 시뮬레이션
while q:
    time, value, y, x = heapq.heappop(q)

    # 목표 시간이 되면 중단
    if time == S:
        break

    # 4방향으로 전염 시도
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 유효한 위치 && 아직 전염되지 않은 칸이면 전염
        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0:
            board[ny][nx] = value
            heapq.heappush(q, (time + 1, value, ny, nx))

# 정답 출력 (1-based index → 0-based index 보정)
print(board[X - 1][Y - 1])