from collections import deque


def solution(begin, target, words):
    # target 단어가 words 리스트에 없으면 변환 불가능
    if target not in words:
        return 0
    
    # 각 단어의 방문 여부를 기록하는 딕셔너리
    visited = {}
    for w in words:
        visited[w] = False
    
    # BFS를 위한 큐: (현재 단어, 변환 횟수)
    q = deque([(begin, 0)])
    
    # 큐가 빌 때까지 탐색
    while q:
        cur, count = q.popleft()  # 현재 단어와 변환 횟수
        
        # 목표 단어에 도달하면 변환 횟수 반환
        if cur == target:
            return count
        
        # 아직 방문하지 않은 단어들만 필터링
        visited_word = [w for w in words if visited[w] == False]
        
        # 방문하지 않은 각 단어에 대해
        for nw in visited_word:
            match_count = 0  # 현재 단어와 일치하는 글자 수
            
            # 각 위치의 글자를 비교
            for i in range(len(nw)):
                if nw[i] == cur[i]:
                    match_count += 1
            
            # 정확히 한 글자만 다른 경우 (변환 가능한 단어)
            # 예: "hot" -> "dot" (h와 d만 다름, 나머지 2글자 일치)
            if match_count == len(nw) - 1:
                visited[nw] = True  # 방문 처리
                q.append((nw, count + 1))  # 큐에 추가 (변환 횟수 +1)
    
    # 목표 단어에 도달할 수 없는 경우
    return 0