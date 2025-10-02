# 백준 15686번: 치킨 배달
# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

input = sys.stdin.readline

# N: 도시 크기, M: 최대 선택 가능한 치킨집 수
N, M = map(int, input().split())

chicken_map = []
chicken = []  # 치킨집 위치 리스트
home = []     # 집 위치 리스트

# 도시 정보 입력
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            home.append([j, i])     # 집 위치 (x, y)
        elif row[j] == 2:
            chicken.append([j, i])  # 치킨집 위치 (x, y)
    chicken_map.append(row)

# 가능한 치킨집 조합 생성
조합 = list(combinations(chicken, M))

min_value = sys.maxsize  # 도시의 치킨 거리 최솟값

# 각 조합에 대해 도시의 치킨 거리 계산
for chick_comb in 조합:
    chicken_dist = []

    for h in home:
        hr, hc = h
        min_cd = sys.maxsize  # 집과 가장 가까운 치킨집 거리

        for c in chick_comb:
            cr, cc = c
            cd = abs(hr - cr) + abs(hc - cc)  # 맨해튼 거리
            min_cd = min(min_cd, cd)  # 가장 가까운 거리 갱신

        chicken_dist.append(min_cd)  # 해당 집의 치킨 거리 저장

    min_value = min(sum(chicken_dist), min_value)  # 도시 치킨 거리 최소 갱신

# 결과 출력
print(min_value)