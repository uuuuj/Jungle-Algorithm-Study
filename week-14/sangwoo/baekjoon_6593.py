import sys
from collections import deque

input = sys.stdin.readline

# 3차원 이동 (6방향: 동서남북상하)
dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1 ,1]

while True:
    # L: 층 수, R: 행 수, C: 열 수
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break  # 종료 조건

    building = []     # 3차원 빌딩 구조
    floor = []        # 현재 층 구조 저장
    s_position = []   # 시작 지점 (z, y, x)
    e_position = []   # 도착 지점 (z, y, x)
    time = []         # 방문 여부 + 시간 저장 배열

    # 시간 배열 초기화: L층 R행 C열
    for l in range(L):
        f = [[0 for _ in range(C)] for _ in range(R)]
        time.append(f)

    # 빌딩 구조 입력 받기
    while True:
        row = input().rstrip()

        if row == '':
            building.append(floor)  # 현재 층 저장
            floor = []              # 다음 층 초기화
        else:
            if 'S' in row:
                # 시작 위치 찾기 (층, 행, 열)
                s_position = [len(building), len(floor), row.index('S')]
            if 'E' in row:
                # 도착 위치 찾기
                e_position = [len(building), len(floor), row.index('E')]
            floor.append(row)

        if len(building) == L:
            break  # 모든 층 입력 완료

    # BFS 탐색 시작
    q = deque([s_position])  # 시작 위치 큐에 넣기

    while q:
        z, y, x = deque.popleft(q)  # 현재 위치

        for i in range(6):  # 6방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 범위 내 & 방문 전 & 벽이 아닐 경우
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L and time[nz][ny][nx] == 0 and building[nz][ny][nx] != "#":
                time[nz][ny][nx] = time[z][y][x] + 1  # 시간 증가
                deque.append(q, [nz, ny, nx])        # 큐에 추가

    ez, ey, ex = e_position  # 도착 위치

    if time[ez][ey][ex] == 0:
        print('Trapped!')  # 도착 못함
    else:
        print(f'Escaped in {time[ez][ey][ex]} minute(s).')  # 탈출 시간 출력
