# 백준 9205번: 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

import sys
from collections import deque

input = sys.stdin.readline

# BFS 탐색 함수: 집(h) → 페스티벌 장소(r)로 갈 수 있는지 확인
def bfs(h, r, shops):
    q = deque([h])                     # 시작 위치: 집
    visited = [False for _ in shops]  # 편의점 방문 여부 기록

    while q:
        x1, y1 = q.popleft()           # 현재 위치 꺼냄
        xr, yr = r

        # 현재 위치에서 페스티벌까지 갈 수 있는 경우
        if abs(xr - x1) + abs(yr - y1) <= 1000:
            return 'happy'

        # 모든 편의점 탐색
        for i in range(n):
            x2, y2 = shops[i]

            # 1000m 이내이고 아직 방문하지 않은 편의점이면 큐에 추가
            if abs(x1 - x2) + abs(y1 - y2) <= 1000 and not visited[i]:
                visited[i] = True
                q.append(shops[i])

    return 'sad'  # 모든 경로에서 도달 불가

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    n = int(input())                         # 편의점 개수
    h = list(map(int, input().split()))     # 집 좌표
    shops = [list(map(int, input().split())) for _ in range(n)]  # 편의점 좌표들
    r = list(map(int, input().split()))     # 도착지(페스티벌) 좌표

    print(bfs(h, r, shops))