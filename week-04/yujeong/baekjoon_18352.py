from collections import deque
import sys
input = sys.stdin.readline

# 1. 입력 받기
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 2. 그래프(인접 리스트) 구성
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# 3. 거리 배열 초기화: 아직 방문하지 않은 도시는 -1
distance = [-1] * (N + 1)
distance[X] = 0

# 4. BFS 준비
queue = deque([X])

# 5. BFS 수행하며 각 도시까지의 최단 거리 계산
while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if distance[nxt] == -1:        # 아직 방문 안 했으면
            distance[nxt] = distance[cur] + 1
            queue.append(nxt)

# 6. 거리 K인 도시들만 골라서 정렬
result = [i for i in range(1, N + 1) if distance[i] == K]
result.sort()

# 7. 출력
if result:
    for city in result:
        print(city)
else:
    print(-1)
