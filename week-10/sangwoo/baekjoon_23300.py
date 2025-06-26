import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

back = deque()
front = deque()
cur = '0'  # cur을 문자열로

for _ in range(Q):
    operation = input().split()

    if operation[0] == 'B':
        if back:
            front.appendleft(cur)
            cur = back.pop()

    elif operation[0] == 'F':
        if front:
            back.append(cur)
            cur = front.popleft()

    elif operation[0] == 'A':
        if cur:
            back.append(cur)
        cur = operation[1]
        front = deque()  # 앞으로 가기 히스토리 초기화

    elif operation[0] == 'C':
        new_back = deque()
        last = None
        for page in back:
            if page != last:
                new_back.append(page)
                last = page
        back = new_back

# 출력
print(cur)
print(' '.join(reversed(back)) if back else '-1')
print(' '.join(front) if front else '-1')