# https://school.programmers.co.kr/learn/courses/30/lessons/12987

import heapq
from collections import deque


def solution(N, road, K):
    # 각 마을까지의 최소 비용 초기화
    costs = [float("inf")] * (N + 1)
    costs[1] = 0  # 1번 마을에서 시작하므로 거리 0
    
    # 그래프 구성 (양방향)
    graph = [[] for _ in range(N + 1)]
    for n1, n2, value in road:
        graph[n1].append((n2, value))
        graph[n2].append((n1, value))
    
    # 최소 힙 기반 다익스트라
    q = [(0, 1)]  # (비용, 노드) → 순서 바꿔야 함!

    while q:
        cur_value, cur_n = heapq.heappop(q)

        # 이미 더 작은 비용으로 방문했으면 스킵
        if costs[cur_n] < cur_value:
            continue

        for next_n, next_value in graph[cur_n]:
            total_cost = cur_value + next_value
            if total_cost < costs[next_n]:
                costs[next_n] = total_cost
                heapq.heappush(q, (total_cost, next_n))  # 순서 주의!
    
    # 비용이 K 이하인 마을의 수 세기
    return sum(c <= K for c in costs if c != float('inf'))
