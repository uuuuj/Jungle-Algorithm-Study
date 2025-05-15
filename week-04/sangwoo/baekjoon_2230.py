# 백준 2230번: 수 고르기
# https://www.acmicpc.net/problem/2230

import sys

input = sys.stdin.readline

# 수의 개수 N, 목표 차이 M
N, M = map(int, input().split())

# 수열 입력
nums = [int(input()) for _ in range(N)]

# 오름차순 정렬
nums.sort()

# 투 포인터 초기화
left = 0
right = 0
min_value = sys.maxsize  # 최소 차이 저장

# 두 포인터를 이용해 최소 차이 탐색
while right < N and left < N:
    diff = nums[right] - nums[left]  # 현재 두 수의 차이

    if diff < M:
        # 차이가 M보다 작으면 오른쪽 포인터를 오른쪽으로 이동시켜 차이를 증가시킴
        right += 1
    else:
        # 차이가 M 이상이면 조건 만족 → 최소 차이 갱신
        min_value = min(min_value, diff)
        left += 1  # 더 작은 차이 가능성 위해 왼쪽 포인터 이동

# 결과 출력
print(min_value)