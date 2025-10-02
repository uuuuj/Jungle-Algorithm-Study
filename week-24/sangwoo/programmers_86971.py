from collections import deque


# BFS로 연결된 송전탑의 개수를 세는 함수
def bfs(graph, visited, x, count):
    q = deque([x])
    
    while q:
        idx = q.popleft()
        
        # 현재 노드와 연결된 모든 노드 탐색
        for i in graph[idx]:
            if visited[i] == False:
                visited[i] = True  # 방문 처리
                q.append(i)
                count += 1         # 연결된 송전탑 개수 증가
    
    return count


def solution(n, wires):
    # 최소 차이를 저장 (최댓값으로 초기화)
    answer = 100
    
    # 모든 전선을 하나씩 끊어보기
    for i in range(len(wires)):
        # i번째 전선을 제외한 새로운 전선 배열 생성
        new_wires = []
        for j in range(len(wires)):
            if i != j:
                new_wires.append(wires[j])
        
        # 방문 체크 배열 (1번부터 n번까지 사용)
        visited = [False] * (n + 1)
        
        # 각 네트워크의 송전탑 개수를 저장할 리스트
        count = []
        
        # 그래프 초기화 (인접 리스트)
        graph = [[] for _ in range(n + 1)]
        
        # 남은 전선들로 그래프 구성 (양방향)
        for w in new_wires:
            x, y = w
            graph[x].append(y)
            graph[y].append(x)

        # 모든 송전탑에 대해 네트워크 찾기
        for x in range(1, n + 1):
            if visited[x] == False:
                visited[x] = True
                # BFS로 연결된 송전탑 개수 세기
                count.append(bfs(graph, visited, x, 1))

        # 두 네트워크의 송전탑 개수 차이의 절댓값
        # 최솟값 갱신
        answer = min(answer, abs(count[0] - count[1]))
    
    return answer