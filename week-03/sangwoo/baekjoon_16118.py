# 백준 16118번: 달빛 여우
# https://www.acmicpc.net/problem/16118

import heapq
import sys
from collections import deque

input = sys.stdin.readline

# 정점 개수 N, 간선 개수 M 입력
N, M = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력 (양방향, 가중치 2배로 저장)
for _ in range(M):
    n1, n2, v = map(int, input().split())
    v *= 2  # 여우와 늑대의 속도차를 고려해 가중치를 2배로 저장
    graph[n1].append((n2, v))
    graph[n2].append((n1, v))

### 여우의 다익스트라 ###
fox = [float('inf')] * (N + 1)  # 여우의 최단거리 테이블
fox[1] = 0  # 출발점

hq = [(0, 1)]  # (누적 거리, 현재 위치)

while hq:
    dist, cur = heapq.heappop(hq)

    if dist > fox[cur]:
        continue

    for to, cost in graph[cur]:
        new_dist = dist + cost
        if new_dist < fox[to]:
            fox[to] = new_dist
            heapq.heappush(hq, (new_dist, to))

### 늑대의 다익스트라 ###
# wolf[i][0]: i번 노드에 빠르게 도착한 최소 거리
# wolf[i][1]: i번 노드에 느리게 도착한 최소 거리
wolf = [[float('inf')] * 2 for _ in range(N + 1)]
wolf[1][0] = 0  # 시작 지점은 빠른 속도로 시작

hq = [(0, 1, True)]  # (누적 거리, 현재 위치, 다음 이동이 빠른가 여부)

while hq:
    dist, cur, is_fast = heapq.heappop(hq)

    # 이미 더 짧은 거리로 도달한 경우 스킵
    if is_fast and dist > wolf[cur][0]:
        continue
    if not is_fast and dist > wolf[cur][1]:
        continue

    for to, cost in graph[cur]:
        if is_fast:
            # 현재 빠르게 이동 → 다음은 느리게 이동
            next_cost = cost // 2 + dist
            if next_cost < wolf[to][1]:
                wolf[to][1] = next_cost
                heapq.heappush(hq, (next_cost, to, False))
        else:
            # 현재 느리게 이동 → 다음은 빠르게 이동
            next_cost = cost * 2 + dist
            if next_cost < wolf[to][0]:
                wolf[to][0] = next_cost
                heapq.heappush(hq, (next_cost, to, True))

### 결과 계산 ###
# 여우가 더 빨리 도착한 정점의 개수 세기
answer = 0
for i in range(2, N + 1):
    if fox[i] < min(wolf[i]):  # 여우의 최단 거리가 늑대의 빠른/느린 경우보다 모두 짧다면
        answer += 1

print(answer)