# 백준 6593번: 상범 빌딩
# https://www.acmicpc.net/problem/6593

import sys
from collections import deque

input = sys.stdin.readline

# 3차원 이동 방향 (동, 북, 서, 남, 위, 아래)
dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    L, R, C = map(int, input().split())  # L: 층 수, R: 행, C: 열
    if L == 0 and R == 0 and C == 0:
        break  # 종료 조건

    building = []        # 건물 구조 (3차원 리스트)
    floor = []           # 현재 층의 행 리스트
    s_position = []      # 시작 위치 (S)
    e_position = []      # 종료 위치 (E)

    # 시간(방문 거리) 정보 초기화
    time = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    while True:
        row = input().rstrip()

        if row == '':  # 빈 줄이면 층 하나 끝남
            building.append(floor)
            floor = []
        else:
            if 'S' in row:
                s_position = [len(building), len(floor), row.index('S')]  # 시작 위치 저장
            if 'E' in row:
                e_position = [len(building), len(floor), row.index('E')]  # 도착 위치 저장
            floor.append(row)

        if len(building) == L:  # 모든 층을 입력받았으면 종료
            break

    # BFS 시작
    q = deque([s_position])

    while q:
        z, y, x = q.popleft()

        for i in range(6):  # 6방향 이동
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 유효한 위치 && 아직 방문하지 않음 && 벽이 아님
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L:
                if time[nz][ny][nx] == 0 and building[nz][ny][nx] != '#':
                    time[nz][ny][nx] = time[z][y][x] + 1  # 거리 기록
                    q.append([nz, ny, nx])

    ez, ey, ex = e_position

    # 도착 지점에 도달하지 못했으면
    if time[ez][ey][ex] == 0:
        print('Trapped!')
    else:
        print(f'Escaped in {time[ez][ey][ex]} minute(s).')