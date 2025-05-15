# 백준 1806번: 부분합
# https://www.acmicpc.net/problem/1806

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
cur = 0
length = sys.maxsize

for right in range(N):
    cur += nums[right]  # 오른쪽 포인터 확장하며 누적합 추가

    while cur >= S:  # 합이 조건을 만족하면 왼쪽 포인터 이동
        length = min(length, right - left + 1)
        cur -= nums[left]
        left += 1

# 조건을 만족하는 부분합이 없을 경우 0 출력
print(length if length != sys.maxsize else 0)