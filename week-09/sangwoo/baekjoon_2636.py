# 백준 2636번: 치즈
# https://www.acmicpc.net/problem/2636

import sys
from collections import deque

input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 입력
r, c = map(int, input().split())
board = []
total_cheese = 0

# 보드 입력 및 전체 치즈 수 카운트
for _ in range(r):
    row = list(map(int, input().split()))
    board.append(row)
    total_cheese += sum(row)

# 외부 공기와 닿은 치즈를 찾고 녹이는 BFS 함수
def bfs():
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[0][0] = True

    q = deque([[0, 0]])
    melt = set()  # 이번에 녹일 치즈 좌표 모음

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내이면서 방문 안 한 경우
            if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    melt.add((nx, ny))  # 치즈를 녹이기 후보에 추가
                else:
                    visited[ny][nx] = True
                    q.append([nx, ny])

    # 녹일 치즈 좌표에 대해 보드에서 제거
    for x, y in melt:
        board[y][x] = 0

    return len(melt)  # 이번에 녹인 치즈 수 반환

# 시뮬레이션 시작
time = 1  # 첫 시간
while True:
    cur_melt_cheeses = bfs()  # 이번 시간에 녹인 치즈 수
    total_cheese -= cur_melt_cheeses

    if total_cheese == 0:
        print(time)                # 모든 치즈가 녹는 데 걸린 시간
        print(cur_melt_cheeses)   # 마지막에 녹은 치즈 조각 수
        break

    time += 1