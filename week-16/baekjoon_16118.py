import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [ [] for _ in range(N + 1) ]

for i in range(1, N + 1):
  graph[i] = []

for _ in range(M):
  n1, n2, v = map(int, input().split())
  v *= 2
  graph[n1].append((n2, v))
  graph[n2].append((n1, v))

fox = [ float('inf') ] * (N + 1)
fox[1] = 0

hq = [(0, 1)]

while hq:
  dist, cur = heapq.heappop(hq)

  if dist > fox[cur]:
    continue

  for to, cost in graph[cur]:
    new_dist = dist + cost
    if new_dist < fox[to]:
      fox[to] = new_dist
      heapq.heappush(hq, (new_dist, to))

wolf = [ [float('inf')] * 2 for _ in range(N + 1) ]
wolf[1][0] = 0

hq = [(0, 1, True)]

while hq:
  dist, cur, is_fast = heapq.heappop(hq)

  if is_fast and dist > wolf[cur][0]: continue
  if not is_fast and dist > wolf[cur][1]: continue


  for to, cost in graph[cur]:
    if is_fast:
      next_cost = cost // 2 + wolf[cur][0]
      if next_cost < wolf[to][1]:
        wolf[to][1] = next_cost
        heapq.heappush(hq, (next_cost, to, False))

    else :
      next_cost = cost * 2 + wolf[cur][1]
      if next_cost < wolf[to][0]:
        wolf[to][0] = next_cost
        heapq.heappush(hq, (next_cost, to, True))

answer = 0
for i in range(2, N + 1):
    if fox[i] < min(wolf[i]):
        answer += 1
print(answer)