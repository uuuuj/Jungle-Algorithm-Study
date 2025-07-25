import sys
from collections import deque

# 방향 벡터: 오른쪽, 아래, 왼쪽, 위
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

input = sys.stdin.readline

N = int(input())  # 지도의 크기 N x N

# 지도 정보 입력 (문자열을 정수 리스트로 변환)
ground = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 방문 여부를 체크할 배열
visited = [[False] * N for _ in range(N)]

# 각 단지의 집의 수를 저장할 리스트
buildings = []

# DFS 함수 정의
def count_appart_dfs(x, y, count):
    # 상하좌우 4방향을 탐색
    for i in range(4):
        nx = x + DX[i]
        ny = y + DY[i]

        # 지도 범위 안에 있고, 아직 방문하지 않았으며, 집이 있는 경우
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and ground[ny][nx]:
            visited[ny][nx] = True  # 방문 처리
            count = count_appart_dfs(nx, ny, count + 1)  # 재귀적으로 연결된 집 탐색

    return count  # 해당 단지의 총 집 수 반환

# 전체 지도를 돌면서 단지 탐색 시작
for y in range(N):
    for x in range(N):
        if ground[y][x] and not visited[y][x]:  # 집이 있으면서 방문하지 않은 경우
            visited[y][x] = True  # 시작점을 방문 처리
            count = count_appart_dfs(x, y, 1)  # 현재 집도 포함하여 count 시작
            buildings.append(count)  # 단지의 집 수 저장

# 정렬된 결과 출력
buildings.sort()
print(len(buildings))  # 총 단지 수
print(*buildings, sep='\n')  # 각 단지 내 집의 수를 오름차순으로 출력
