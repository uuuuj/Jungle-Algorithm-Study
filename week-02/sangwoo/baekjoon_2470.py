# https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline

# 용액의 수 입력
N = int(input())

# 용액 리스트 입력 후 정렬
liqs = sorted(list(map(int, input().split())))

# 투 포인터 초기값 설정
right = N - 1
left = 0

# 초기 최적값 설정
res_right = right
res_left = left
min_abs = abs(liqs[left] + liqs[right])  # 현재 두 용액의 합의 절댓값

# 투 포인터 탐색 시작
while True:
    total = liqs[right] + liqs[left]  # 두 용액의 합 계산

    # 더 0에 가까운 조합이면 정답 갱신
    if abs(total) < min_abs:
        res_left = left
        res_right = right
        min_abs = abs(total)

    # 두 용액의 합이 0이면 가장 이상적인 조합이므로 종료
    if total == 0:
        break
    # 합이 0보다 크면 값을 줄이기 위해 오른쪽 포인터 이동
    elif total > 0:
        right -= 1
    # 합이 0보다 작으면 값을 키우기 위해 왼쪽 포인터 이동
    else:
        left += 1

    # 포인터가 만나면 더 이상 비교할 수 없으므로 종료
    if left == right:
        break

# 결과 출력
print(liqs[res_left], liqs[res_right])
