# https://www.acmicpc.net/problem/14503

# i, j
'''
   북0
서3    동1
   남2
'''
#로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

N, M = map(int, input().split()) # 방의 크기 N(세로), M(가로)
r, c, d = map(int, input().split()) # 로봇 청소기좌표 (r, c), 방향 d (0 북쪽,1 동쪽, 2 남쪽, 3 서쪽)
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

# 순서 : 북동남서,  반시계: 북서남동북
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
cleaned = 0

while True:
    if grid[r][c] == 0:
        grid[r][c] = 2
        cleaned += 1
    has_clean_space = False
    for i in range(4):
        check_r = r + dx[i]
        check_c = c + dy[i]
        if 0 <= check_r < N and 0 <= check_c < M and grid[check_r][check_c] == 0:
            has_clean_space = True
            break

    if has_clean_space:
        d = (d + 3) % 4 # 반시계 케이스
        nr = r + dx[d]
        nc = c + dy[d]
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
            r, c = nr, nc
    else: # 후진 케이스
        back_r = r + dx[(d+2)%4]
        back_c = c + dy[(d+2)%4]

        if 0 <= back_r < N and 0 <= back_c < M and grid[back_r][back_c] != 1:
            r, c = back_r, back_c
        else:
            break

print(cleaned)
