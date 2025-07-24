import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
galaxy = [list(map(int, input().split())) for _ in range(N)]


galaxy_res = defaultdict(int)

for g in galaxy:
    sorted_index = sorted(range(M), key= lambda i : g[i])
    ranks = [ 0 ] * M
    rank = 1

    for i in range(M):
      if i > 0 and g[sorted_index[i]] != g[sorted_index[i - 1]]:
        rank += 1

      ranks[sorted_index[i]] = rank


    galaxy_res[tuple(ranks)] += 1

total = 0
for count in galaxy_res.values():
    total += count * (count - 1) // 2

print(total)
