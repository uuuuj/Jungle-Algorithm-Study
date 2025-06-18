import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
houses, chickens = [], []

for r in range(N):
    for c, v in enumerate(map(int, sys.stdin.readline().split()))
        if v == 1:
            houses.append((r, c))
        elif v == 2:
            chickens.append((r, c))


best = float('inf')     # 최소 도시 치킨 거리

for keep in combinations(chickens, M):
    city = 0
    # hr, hc = 집 좌표의 y축, x축
    # cr, cc = 치킨집 좌표의 y축, x축문
    for hr, hc in houses:
        # 각 집에서 가장 가까운 (살려둘) 치킨집까지의 거리
        dist = min(abs(hr - cr) + abs(hc -cc) for cr, cc in keep)
        city += dist

        # 이미 best 보다 커지면 바로 중단
        if city >= best:
            break
    best = min(best, city)

print(best)
