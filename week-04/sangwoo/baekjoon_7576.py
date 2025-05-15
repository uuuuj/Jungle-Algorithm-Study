# 백준 7576번: 토마토
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

# 상, 우, 하, 좌 방향 정의
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

input = sys.stdin.readline

# M: 열(가로), N: 행(세로)
M, N = map(int, input().split())

# BFS를 위한 큐 초기화
q = deque()

# 토마토 상태 배열 (2차원 리스트)
tomato = []

# 입력 받으며 익은 토마토(1)의 좌표를 큐에 미리 저장
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        if row[x] == 1:
            q.append([x, y, 0])  # (x좌표, y좌표, 익은 날짜)
    tomato.append(row)

last_day = 0  # 모든 토마토가 익는 데 걸리는 최대 일수

# BFS 시작
while q:
    x, y, day = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있고, 안 익은 토마토(0)일 경우 익히기
        if 0 <= nx < M and 0 <= ny < N and tomato[ny][nx] == 0:
            tomato[ny][nx] = 1         # 익힘 처리
            q.append([nx, ny, day + 1])  # 다음 날 익는 것으로 큐에 추가
            last_day = max(last_day, day + 1)  # 최대 날짜 갱신

# 익지 않은 토마토가 있는지 검사
is_all_done = True
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 0:
            is_all_done = False  # 익지 않은 토마토가 있으면 실패

# 결과 출력
if is_all_done:
    print(last_day)  # 모든 토마토가 익는 데 걸린 일수
else:
    print(-1)  # 익지 못한 토마토가 있음