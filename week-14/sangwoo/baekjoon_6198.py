import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 빌딩의 수 입력

res = [ 0 for _ in range(N) ]  # 각 건물에서 볼 수 있는 건물 수를 저장할 리스트

# 빌딩의 높이를 입력받아 deque로 저장 (빠른 pop을 위해)
buildings = deque([ int(input()) for _ in range(N) ])

stack = []  # (인덱스, 높이)를 저장할 스택

# 빌딩을 오른쪽에서 왼쪽으로 역순으로 순회
for i, h in list(enumerate(buildings))[::-1]:
  if len(stack) == 0:
    # 스택이 비어있으면 현재 건물을 스택에 추가
    stack.append((i, h))
  else:
    smaller_building = 0  # 현재 건물이 볼 수 있는 건물 수

    # 현재 건물보다 낮은 건물은 모두 볼 수 있으므로 pop하면서 count
    while stack[-1][1] < h:
      pre_i, _ = stack.pop()
      smaller_building += 1 + res[pre_i]  # res[pre_i]는 이전 건물이 볼 수 있던 개수

      if len(stack) == 0:
        break  # 스택이 비면 종료

    # 현재 건물에서 볼 수 있는 건물 수 기록
    res[i] = smaller_building

    # 현재 건물을 스택에 추가
    stack.append((i, h))

# 모든 건물에서 볼 수 있는 건물 수의 총합 출력
print(sum(res))
