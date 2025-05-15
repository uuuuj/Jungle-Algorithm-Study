import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())    # 가로 세로 크기 받기
graph = [list(map(int, input().split())) for _ in range(n)] # n줄을 읽어 2차원 리스트에 저장

# graph[i][j] 값이 
# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 없는 칸

## 처음 익은 토마토를 찾자

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# 이미 익어있는 [i, j] 좌표를 모두 queue에 담기
# "첫날" 익은 토마토들이 모두 출발점(start node)이 된다

## BFS로 토마토 익히기

def bfs():
    while queue:
        x, y = queue.popleft()

        # 4방향 : 위(-1, 0), 아래(+1, 0), 왼쪽(0, -1), 오른쪽(0, +1)

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            
            # 위, 아래, 왼쪽, 오른쪽을 순서대로 훑기
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위 안에 있고, 익지 않은 토마토(0)라면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 익은 날짜 표시 : 현재 토마토의 날짜 + 1
                # graph[x][y] : queue에 넣어두었던, 익은 토마토의 값에 + 1로 업데이트트
                graph[nx][ny] = graph[x][y] + 1 
                # 이미 익었던 토마토로 인해 익은 토마토가 되었으니 queue에 넣어준다
                queue.append((nx, ny))
    

bfs()

day = 0

for row in graph:
    for cell in row:
        if cell == 0:
            print(-1)
            exit()  # 하나라도 익지 않은 토마토가 남았다면 -1 출력
    
    day = max(day, max(row))    # 그래프에 남아있는 가장 큰 숫자가 마지막으로 익은 날날

print(day - 1)  # 토마토가 익은 것을 1로 표현했고, 곧 시작 날짜가 1이었음.

# 최댓값이 5라고 가정한다면, 1, 2, 3, 4, 5 실제로는 4일이 걸린 것
# 그래서 -1


