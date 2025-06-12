# 백준 1240번: 노드사이의 거리
# https://www.acmicpc.net/problem/1240

import sys

input = sys.stdin.readline

# N: 노드 수, M: 거리 계산 쿼리 수
N, M = map(int, input().split())

# 인접 리스트로 트리 표현
tree = [[] for _ in range(N + 1)]

# 트리 간선 정보 입력
for _ in range(N - 1):
    f, t, v = map(int, input().split())
    tree[f].append((t, v))
    tree[t].append((f, v))

# 거리 계산 요청 목록
dists = [list(map(int, input().split())) for _ in range(M)]

# 각 쿼리에 대해 DFS로 거리 계산
for n1, n2 in dists:
    dist = [0 for _ in range(N + 1)]  # 각 노드까지의 거리 저장
    visited = [False] * (N + 1)       # 방문 여부 체크

    q = [n1]
    visited[n1] = True

    while q:
        cur = q.pop()

        if cur == n2:
            print(dist[n2])
            break

        for nn, nv in tree[cur]:
            if not visited[nn]:
                visited[nn] = True
                dist[nn] = dist[cur] + nv
                q.append(nn)