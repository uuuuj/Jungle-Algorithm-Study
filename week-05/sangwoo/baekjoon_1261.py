# 백준 1261번: 알고스팟
# https://www.acmicpc.net/problem/1261

import heapq
import sys

input = sys.stdin.readline

# 방향 벡터 (우, 하, 좌, 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# M: 가로, N: 세로
M, N = map(int, input().split())

# 방 구조 입력 (0: 빈 방, 1: 벽)
room = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 방문 여부 체크 배열
visited = [[False for _ in range(M)] for _ in range(N)]

# 최소 벽 부순 횟수 기준으로 탐색하기 위한 우선순위 큐
q = [[0, 0, 0]]  # [벽 부순 횟수, x, y]
visited[0][0] = True

# 다익스트라 방식의 BFS (우선순위 큐 사용)
while q:
    cost, x, y = heapq.heappop(q)

    # 도착지 도달 시 벽을 부순 최소 횟수 출력
    if x == M - 1 and y == N - 1:
        print(cost)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있고, 아직 방문하지 않은 칸이면
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True

            if room[ny][nx] == 0:
                # 벽이 없으면 비용 유지
                heapq.heappush(q, [cost, nx, ny])
            else:
                # 벽이 있으면 벽을 부수고 비용 +1
                heapq.heappush(q, [cost + 1, nx, ny])