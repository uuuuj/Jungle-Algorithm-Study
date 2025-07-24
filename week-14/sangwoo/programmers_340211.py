from collections import Counter  # 좌표별 중복 카운트를 위한 모듈


def solution(points, routes):
    
    answer = 0  # 충돌(겹치는 위치) 횟수 카운트
    route_detail = []  # 각 경로가 지나는 좌표들을 시간 순서대로 저장
    max_length = 0  # 가장 긴 경로의 길이를 저장

    for r in routes:  # 각 경로에 대해 처리
        path = []  # 현재 경로가 지나가는 좌표 리스트

        # 경로에 있는 점들을 순서대로 순회
        for p in range(len(r) - 1):
            sr, sc = points[r[p] - 1]      # 시작 좌표 (points는 0-indexed, routes는 1부터 시작)
            er, ec = points[r[p + 1] - 1]  # 도착 좌표

            # 세로(행 방향) 먼저 이동
            while sr != er:
                path.append((sr, sc))  # 이동 중 위치 저장
                sr = sr - 1 if sr > er else sr + 1  # 한 칸씩 er 방향으로 이동

            # 가로(열 방향) 이동
            while sc != ec:
                path.append((sr, sc))  # 이동 중 위치 저장
                sc = sc - 1 if sc > ec else sc + 1  # 한 칸씩 ec 방향으로 이동
            
        path.append((sr, sc))  # 마지막 도착 좌표도 추가
        route_detail.append(path)  # 경로 저장
        max_length = max(max_length, len(path))  # 가장 긴 경로 업데이트

    # 시간대별로 각 경로가 지나간 위치를 확인
    for i in range(max_length):
        cur_points = []  # i번째 시간에 각 경로가 있는 좌표

        for x in route_detail:
            if len(x) > i:  # 경로가 i 시간까지 존재하는 경우
                cur_points.append(x[i])  # 해당 시간의 좌표 수집

        pointer_counter = Counter(cur_points)  # 좌표별로 몇 명이 지나가는지 카운트

        for c in pointer_counter.values():
            if c > 1:  # 두 명 이상이 같은 좌표에 있으면 충돌 발생
                answer += 1  # 충돌 횟수 증가

    return answer  # 최종 충돌 횟수 반환
