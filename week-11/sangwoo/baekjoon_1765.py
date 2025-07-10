import sys
from collections import deque

dx = [1, 0]
dy = [0, 1]

input = sys.stdin.readline

N = int(input())

board = []

for i in range(N):
  row = [ int(i) if str.isdigit(i) else i for i in input().rstrip().split() ]
  board.append(row)

def bfs(is_max):
  init_value = -1000000 if is_max else sys.maxsize
  res = [ [  init_value for _ in range(N) ] for _ in range(N) ]

  q = deque([[0, 0, '', board[0][0]]])
  res[0][0] = board[0][0]

  while q:
    x, y, op, cur = deque.popleft(q)

    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if str.isdigit(str(board[ny][nx])):
          if op == '+':
            value = cur + board[ny][nx]
          elif op == '-':
            value = cur - board[ny][nx]
          else:
            value = cur * board[ny][nx]
          
          if is_max:
            if res[ny][nx] <= value:
              res[ny][nx] = value
              deque.append(q, [nx, ny, '', res[ny][nx]])
          else:
            if res[ny][nx] >= value:
              res[ny][nx] = value
              deque.append(q, [nx, ny, '', res[ny][nx]])

        else:
          deque.append(q, [nx, ny, board[ny][nx], cur])

  return res[N - 1][N - 1]

print(bfs(True), bfs(False))
