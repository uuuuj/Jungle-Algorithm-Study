# 공통 baekjoon 2667 단지번호붙이기 (통과)
import sys
sys.setrecursionlimit(10000)

N = int(input())
map = []
for i in range(N):
    line = input()
    map.append(list(line))
visited = [[False] * N for _ in range(N)]

Village = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if map[nx][ny] == '1' and not visited[nx][ny]:
                count += dfs(nx, ny)
    return count

for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and not visited[i][j]:
            count = dfs(i, j)
            Village.append(count)

Village.sort()
print(len(Village))
for i in Village:
    print(i)
