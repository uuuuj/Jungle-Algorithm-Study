import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [ [] for _ in range(N + 1)]

for _ in range(M):
  n1, n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)

visited = [ False ] * (N + 1)

graph_count = 0
cut_count = 0

for i in range(1, N + 1):
  if visited[i]:
    continue

  graph_count += 1

  q = deque([(i, 0)])
  visited[i] = True

  while q:
    cur, pre = deque.popleft(q)

    for node in graph[cur]:
      if visited[node] == False:
        visited[node] = True
        deque.append(q, (node, cur))
      else:
        if (node != pre and pre != 0):
          cut_count += 1

print(graph_count - 1 + cut_count // 2)