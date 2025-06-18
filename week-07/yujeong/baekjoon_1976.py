import sys
from collections import deque

input = sys.stdin.readline

# 트리를 쭉 늘어뜨려 직선으로 만들었을때의 길이가 지름이다.
# 그 상태를 막대라고 생각하면, 막대 위 아무 지점에서 가장 먼곳을 재면 언제나 막대 끝이다
# 그 막대 끝에서 다시 제일 먼 곳을 재면 반대쪽 끝을 만나는건 당연하다.
# 그 사이의 거리가 트리의 지름이다.

def bfs(start, adj):
    # start : 출발 정점 번호
    # adj : 인접 노드 목록

    visited = [-1] * len(adj)   # -1일 경우 미방문, 또는 누적 거리
    visited[start] = 0  # 시작점까지 거리는 0
    q = deque([start])

    far_node = start    # 현재까지 가장 먼 정점

    while q:
        cur = q.popleft()
        for nxt, w in adj[cur]:     # cur와 인접한 노드들과 거리를 살펴보기
            if visited[nxt] == -1:      # 미방문 했을 경우
                visited[nxt] = visited[cur] + w     # cur와 인접한 노드의 거리는 현재 노드의 거리에, 현재 노드와 인접한 노드1번의 거리의 합
                q.append(nxt)       # 인접 노드를 큐에 넣어 다음으로 살펴볼 노드 리스트에 추가
                if visited[nxt] > visited[far_node]: # 지금까지 본 것 중 가장 먼 노드보다, 현재까지의 누적 거리가 더 크다면
                    far_node = nxt      # 가장 먼 노드는 nxt가 된다.
    return far_node, visited[far_node]      # 가장 먼 노드와 누적거리를 반환

def main():
    N = int(input())
    if N == 1:
        print(0)
        return

    # 인접 노드 및 간선 거리를 기록한 그래프 내용 기록하기(0번은 비우고 1~N번까지만 사용)
    adj = [[] for _ in range(N+1)]

    # 간선 읽어서 인접 노드 목록 채우기
    for _ in range(N - 1):
        parent, child, dist = map(int, input().split())     # 부모, 자식, 거리
        adj[parent].append((child, dist))   
        adj[child].append((parent, dist))   

    # 1번에서 가장 먼 정점 far1 찾기
    far1, _ = bfs(1, adj)

    # far1에서 가장 먼 정점 far2와 거리 찾기

    far2, dia = bfs(far1, adj)

    print(dia)


if __name__ == "__main__":
    main()
