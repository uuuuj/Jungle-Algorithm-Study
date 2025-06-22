# 백준 1967번: 트리의 지름
# https://www.acmicpc.net/problem/1967

import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 노드 개수
N = int(input())

# 그래프 및 거리 정보 초기화
graph = [[] for _ in range(N + 1)]
value = [[] for _ in range(N + 1)]  # 각 노드 기준으로 자식 노드까지의 거리 리스트

# 간선 입력 처리 (방향: 부모 → 자식으로 주어짐)
for _ in range(N - 1):
    f, t, v = map(int, input().split())
    graph[f].append((t, v))  # f에서 t까지 거리 v

# 하위 노드부터 거리 누적
def setLeftAndRightValue(node):
    if not graph[node]:  # 자식이 없으면 리프 노드
        return

    value[node] = []

    for n, nv in graph[node]:
        setLeftAndRightValue(n)  # 자식 먼저 계산
        # 현재 간선을 포함한 자식 노드까지 최대 거리
        lv = nv + (max(value[n]) if value[n] else 0)
        value[node].append(lv)

# 루트 노드에서 시작
setLeftAndRightValue(1)

print(value)

# 트리의 지름 = 어떤 노드를 기준으로 자식으로부터 오는 두 경로 중 가장 긴 두 개의 합
# value 배열에서 가장 큰 두 값을 더한 것들 중 최대값이 정답\
print(list(map(lambda x: sorted(x, reverse=True)[:2], value)))
print(list(map(lambda x: sum(sorted(x, reverse=True)[:2]), value)))

print(max(map(lambda x: sum(sorted(x, reverse=True)[:2]), value)))