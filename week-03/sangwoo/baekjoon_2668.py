# 백준 2668번: 숫자고르기
# https://www.acmicpc.net/problem/2668

import sys
from collections import deque

input = sys.stdin.readline

# 입력받을 숫자의 개수
N = int(input())

# index 1부터 시작하기 위해 0번 인덱스에 0을 넣고 나머지 입력 값을 받음
nums = [0] + [int(input()) for _ in range(N)]

# 조건을 만족하는 숫자들을 담을 집합
answer = set()

# DFS처럼 순환 구조를 따라가며 index와 값을 따로 추적
def get_nums(n, index_nums, pick_nums):
    # 현재 index와 값을 기록
    index_nums.append(n)
    pick_nums.append(nums[n])

    # 아직 방문하지 않은 숫자면 계속 탐색
    if not visited[nums[n]]:
        visited[nums[n]] = True
        return get_nums(nums[n], index_nums, pick_nums)

    # 이미 방문한 숫자를 만나면 종료
    return [index_nums, pick_nums]

# 1부터 N까지 모든 숫자에 대해 반복
for i in range(1, N + 1):
    # 각 시작점마다 방문 배열을 새로 생성
    visited = [False] * (N + 1)

    # 시작점은 방문 처리
    visited[i] = True

    # 현재 시작점에서 사이클 경로 추적
    arr_1, arr_2 = get_nums(i, [], [])

    # 경로에서 index와 값이 같은 집합을 이루면 유효한 사이클
    if set(arr_1) == set(arr_2):
        answer.update(arr_1)  # 정답 집합에 추가

# 결과 출력
print(len(answer))             # 선택된 숫자의 개수
print(*sorted(answer), sep='\n')  # 오름차순으로 숫자 출력