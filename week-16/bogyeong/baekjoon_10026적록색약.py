# https://www.acmicpc.net/problem/10026

'''
적록색약이 아닌 사람이 봤을 때 (빨, 파, 초)
적록색약(빨초, 파랑)

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
5
RRRBB
GGBBB
BBBRR
BBRRR
4 3
'''
import sys
sys.setrecursionlimit(10000)
n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input()))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs_r_g_b(x, y, color, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if grid[nx][ny] == color:
                dfs_r_g_b(nx, ny, color, visited)

def dfs_rg_b(x, y, color, visited):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if color in ['R', 'G'] and grid[nx][ny] in ['R', 'G']:
                dfs_rg_b(nx, ny, color, visited)
            elif color == 'B' and grid[nx][ny] == 'B':
                dfs_rg_b(nx, ny, color, visited)

visited_r_g_b = [[False] * n for _ in range(n)]
r_g_b_count = 0

for i in range(n):
    for j in range(n):
        if not visited_r_g_b[i][j]:
            dfs_r_g_b(i, j, grid[i][j], visited_r_g_b)
            r_g_b_count += 1

visited_rg_b = [[False] * n for _ in range(n)]
rg_b_count = 0

for i in range(n):
    for j in range(n):
        if not visited_rg_b[i][j]:
            dfs_rg_b(i, j, grid[i][j], visited_rg_b)
            rg_b_count += 1

print(r_g_b_count, rg_b_count)
