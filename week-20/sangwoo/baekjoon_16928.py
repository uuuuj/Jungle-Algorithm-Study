import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board_info = {}
visited = [ False for _ in range(0, 101)]

for i in range(1, 101):
  board_info[i] = i

for i in range(N + M):
  f, t = map(int, input().split())
  board_info[f] = t
  

q = deque([])

for i in range(2, 8):
  deque.append(q, (i, 1))
  next_step =  board_info[i]

  visited[next_step] = True
  deque.append(q, (next_step, 1))

while q:
  # print(q)
  # print()
  cur_step, dice_count = deque.popleft(q)

  if cur_step == 100:
    print(dice_count)
    break

  for i in range(1, 7):
    origin_next_value = cur_step + i
    if origin_next_value <= 100:
      next_step =  board_info[cur_step + i]

      if not visited[next_step]:
        visited[next_step] = True
        deque.append(q, (next_step, dice_count + 1))



    