# 연결 요소란? 
# 서로 길을 따라 이동할 수 있는 점 묶음
    # 같은 묶음 안에서는 어느 점에서든 다른 점으로 갈 수 있다
    # 다른 묶음끼리는 길이 전혀 없다
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)    # u와 연결된 노드인 v를 입력
    adj[v].append(u)    # 양방향 연결이기 때문에 v도 마찬가지로 입력

visited = [False] * (N+1)   # 방문했는지 표시

def bfs(start):
    q = deque([start])
    visited[start] = True   # 출발점을 방문했다 표시

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:        # 현재 노드의 모든 연결 노드를 확인
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

components = 0
for node in range(1, N+1):
    if not visited[node]:    # 아직 방문하지 않았다면 새 묶음이다
        bfs(node)
        components += 1 # 묶음 하나 추가!

print(components)

