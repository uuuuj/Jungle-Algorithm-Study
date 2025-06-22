# 백준 24725번: 유사 중위 순회
# https://www.acmicpc.net/problem/24725

import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 노드 수 입력
N = int(input())

# 트리 초기화 (1-indexed)
tree = [[] for _ in range(N + 1)]

# 각 노드의 왼쪽 자식과 오른쪽 자식 입력
for _ in range(N):
    c, l, r = map(int, input().split())
    tree[c] = [l, r]  # c번 노드의 왼쪽 자식 l, 오른쪽 자식 r

visited_order = []

# 유사 중위 순회 함수
def 유사_중위_순회(node):
    if node == -1:
        return
    l, r = tree[node]
    유사_중위_순회(l)
    visited_order.append(node)  # 방문 순서 기록
    유사_중위_순회(r)

# 루트 노드(1번)부터 중위 순회 수행
유사_중위_순회(1)

# BFS를 통해 마지막 중위 순회 노드까지 가는 최소 간선 수를 계산
q = deque([(1, 0)])  # (현재 노드, 지나온 간선 수)

while q:
    cur, 간선_개수 = q.popleft()

    if cur == visited_order[-1]:
        # 전체 왕복 거리에서 마지막 노드까지 간 거리만 빼면 정답
        print((N - 1) * 2 - 간선_개수)
        break

    l, r = tree[cur]

    if l != -1:
        q.append((l, 간선_개수 + 1))

    if r != -1:
        q.append((r, 간선_개수 + 1))