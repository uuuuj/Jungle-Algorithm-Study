# https://www.acmicpc.net/problem/2110

import sys

input = sys.stdin.readline

# 집의 개수 N, 설치할 공유기 개수 C 입력
N, C = map(int, input().split())

# 집들의 좌표를 입력받아 리스트에 저장
home = [int(input()) for _ in range(N)]

# 좌표를 오름차순 정렬
home.sort()

# 이분 탐색 범위 설정
# 최소 거리: 1 (가장 가까운 경우)
# 최대 거리: 가장 먼 두 집의 거리
right = max(home) - min(home)
left = 1

# 최종 결과 (가장 인접한 두 공유기 사이의 최대 거리)
res = 0

# 이분 탐색 시작
while left <= right:
    mid = (right + left) // 2  # 현재 확인할 최소 거리 후보

    cur_home = home[0]  # 첫 번째 집에 공유기 설치
    count = 1  # 설치한 공유기 개수

    # 그 다음 집부터 공유기를 설치할 수 있는지 확인
    for i in range(1, N):
        # 이전에 설치한 집과의 거리가 mid 이상이면 설치 가능
        if home[i] - cur_home >= mid:
            count += 1
            cur_home = home[i]  # 현재 집에 공유기 설치

    # 공유기 C개 이상 설치 가능하면 거리 늘려보기
    if count >= C:
        res = mid  # 가능한 거리 저장
        left = mid + 1  # 더 큰 거리도 가능한지 확인
    else:
        right = mid - 1  # 거리가 너무 커서 설치 못한 경우 → 줄이기

# 결과 출력
print(res)