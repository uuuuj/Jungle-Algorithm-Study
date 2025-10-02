import sys

# 재귀 깊이 제한 증가 (DFS를 위해 필요)
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# N: 학생 수, M: 친구 관계 수, k: 가진 돈
N, M, k = map(int, input().split())

# cost[i]: i번 학생을 친구로 만드는 비용
# 인덱스를 1부터 사용하기 위해 맨 앞에 0 추가
cost = [0] + list(map(int, input().split()))

# 그래프 초기화: 각 학생의 친구 리스트
graph = {}
for i in range(N):
  graph[i + 1] = []

# 친구 관계 입력 (양방향 그래프)
for _ in range(M):
  a, b = map(int, input().split())
  
  graph[a].append(b)  # a의 친구에 b 추가
  graph[b].append(a)  # b의 친구에 a 추가

# 방문 체크 배열 (1번부터 N번까지 사용)
visited = [False] * (N + 1)


# DFS로 연결된 모든 노드를 찾는 함수
def dfs(node, res):
  # 현재 노드와 연결된 모든 친구들을 탐색
  for n in graph[node]:
    if visited[n] == False:
      visited[n] = True  # 방문 처리
      res.append(n)       # 같은 그룹에 추가
      res = dfs(n, res)   # 재귀적으로 연결된 친구들 탐색
  
  return res


# 모든 연결된 그룹(컴포넌트)을 저장할 리스트
linked_node = []

# 모든 학생에 대해 그룹 찾기
for i in range(1, N + 1):
  if visited[i] == False:
    visited[i] = True
    res = dfs(i, [i])      # i와 연결된 모든 학생 찾기
    linked_node.append(res)  # 그룹 저장

# 총 비용 계산
total_cost = 0

# 각 그룹에서 가장 저렴한 학생을 선택
for ln in linked_node:
  # 그룹 내 모든 학생의 비용 중 최소값 선택
  min_cost = min(list(map(lambda x: cost[x], ln)))
  total_cost += min_cost

# 예산 내에서 가능한지 확인
if total_cost <= k:
  print(total_cost)
else:
  print('Oh no')