# 백준 1790번: 수 이어 쓰기 2
# https://www.acmicpc.net/problem/1790

import sys

input = sys.stdin.readline

# N: 마지막 숫자, K: K번째 숫자를 구함
N, K = map(int, input().split())

index = 0
l = K  # 남은 길이 추적용

# 숫자의 자릿수 그룹을 순회 (1자리, 2자리, 3자리...)
while True:
    # 현재 자릿수 그룹의 총 자릿수: (9 * 10^index) * (index + 1)
    next_group = 9 * (10 ** index) * (index + 1)

    if l <= next_group:
        break  # K가 이 그룹 내에 속하면 종료

    l -= next_group  # 다음 그룹으로 넘어갈 준비
    index += 1       # 자릿수 증가

# index: 현재 자리수 - 1
# l: 현재 자리수 그룹 내에서의 K번째 위치

pos = l // (index + 1)         # 해당 자리수 숫자 그룹에서 몇 번째 숫자인지
pospos = l % (index + 1)       # 그 숫자의 몇 번째 자리인지

target = (10 ** index) + pos  # 실제 숫자

# 위치가 숫자의 마지막 자리일 경우
if pospos == 0:
    target -= 1  # 다음 숫자로 넘어가지 않도록 조정
    if target > N:
        print(-1)  # 범위를 초과한 경우
    else:
        print(str(target)[-1])  # 마지막 자리 출력
else:
    if target > N:
        print(-1)  # 범위를 초과한 경우
    else:
        print(str(target)[pospos - 1])  # 해당 자리 출력