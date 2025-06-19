# 백준 1038번: 감소하는 수
# https://www.acmicpc.net/problem/1038

import sys

N = int(input())

# 초기 큐: 1자리 감소하는 수들 (0~9)
q = [[i] for i in range(10)]

count = 0  # 생성된 감소하는 수의 개수

# 예외 처리: N == 0이면 0이 정답
if N == 0:
    print(0)
else:
    while q:
        cur = q.pop(0)
        count += 1

        # N번째 감소하는 수를 찾으면 출력
        if count == N:
            print(''.join(map(str, cur)))
            break

        # 현재 수에서 다음 자릿수 붙이기 (감소 조건 유지)
        for j in range(cur[-1]):
            q.append(cur + [j])

    # N이 전체 감소하는 수의 개수보다 크면 -1 출력
    if N > count:
        print(-1)