# https://www.acmicpc.net/problem/33888
# 문제 이해: 20분
'''
점정: N개
핵심정점: 6개
일반정점 : N-6개
핵심정점은 차수가 3개 or 4개 or 1개
일반정점 : 차수 2
- 즉, 차수가 2가 아닌 정점들은 무조건 핵심 정점
- 차수가 1이면 꼬리
- 차수가 4이면 꼬리뼈, 중심뼈
- 꼬리(F) -> 꼬리뼈(E) -> 중심뼈(C) -> 꼬리뼈와 인접하지 않은 머리(A) -> 나머지 둘중 더 큰것이 오른쪽 날개(D), 작은 것이 왼쪽 날개(B)

'''

from collections import deque


nodes = int(input().strip())

graph = [[] for _ in range(nodes + 1)]

lines = nodes + 3

for _ in range(lines):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

deg = [0] * (nodes + 1)
for i in range(1, nodes + 1):
    deg[i] = len(graph[i])

core_nodes = [i for i in range(1, nodes + 1) if deg[i] != 2]

is_core = [False] * (nodes + 1)
for v in core_nodes:
    is_core[v] = True

core_six = 6
related_core = [[False] * core_six for _ in range(core_six)]

def make_related_core(start_core, tail_core):
    visited = [False] * (nodes + 1)
    q = deque()
    q.append(start_core)
    visited[start_core] = True
    while q:
        point_x = q.popleft()
        for related_x in graph[point_x]:
            if related_x == tail_core:
                return True
            if is_core[related_x]:
                continue
            if not visited[related_x]:
                visited[related_x] = True
                q.append(related_x)
    return False

for i in range(core_six):
    for j in range(i + 1, core_six):
        if make_related_core(core_nodes[i], core_nodes[j]):
            related_core[i][j] = True
            related_core[j][i] = True

deg_core = [0] * core_six
for i in range(core_six):
    for j in range(core_six):
        if related_core[i][j]:
            deg_core[i] += 1

idx_A, idx_B, idx_C, idx_D, idx_E, idx_F = 0, 0, 0, 0, 0, 0

for i in range(core_six):
    if deg_core[i] == 1:
        idx_F = i
        break

for i in range(core_six):
    if related_core[idx_F][i] and deg_core[i] == 4:
        idx_E = i
        break

for i in range(core_six):
    if deg_core[i] == 4 and i != idx_E:
        idx_C = i
        break

for i in range(core_six):
    if i not in (idx_F, idx_E, idx_C) and not related_core[i][idx_E]:
        idx_A = i
        break

BD = []
for i in range(core_six):
    if i not in (idx_F, idx_E, idx_C, idx_A):
        BD.append(i)

if BD[0] < BD[1]:
    idx_B = BD[0]
    idx_D = BD[1]
else:
    idx_B = BD[1]
    idx_D = BD[0]

A = core_nodes[idx_A]
B = core_nodes[idx_B]
C = core_nodes[idx_C]
D = core_nodes[idx_D]
E = core_nodes[idx_E]
F = core_nodes[idx_F]

print(A, B, C, D, E, F)