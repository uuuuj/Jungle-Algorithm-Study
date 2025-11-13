import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
answer = False

def dfs(node, depth):
    global answer
    if depth == 4:
        answer = True
        return
    
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, depth+1)
            if answer:
                return
    visited[node] = False

for i in range(N):
    visited = [False] * N
    dfs(i, 0)
    if answer:
        break

print(1 if answer else 0)
