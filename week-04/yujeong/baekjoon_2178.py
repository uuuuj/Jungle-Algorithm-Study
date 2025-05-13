import sys
from collections import deque

# 큐를 이용해 현재 위치에서 갈 수 있는 모든 인접 칸을 차례로 방문하고
# 그 칸에 시작점으로부터의 거리(몇칸째인지)를 기록해두기

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))    # 시작점을 큐에 넣기

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 안에 있고
            # 길(1)인 칸만 방문
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                # 거리 기록 : 이전 칸 값 + 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]  # 끝 점에 적힌 값이 최단 거리

print(bfs())


