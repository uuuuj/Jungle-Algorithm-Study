import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    n, m = map(int, input().split())
    adj[n].append(m)
    adj[m].append(n)

visited = [False] * (N+1)

def bfs(start):
    virus = 0
    q = deque([start])
    visited[start] = True   # 출발점을 방문했다 표시

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                virus += 1
    return virus

print(bfs(1))