import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

iceberg = [ list(map(int, input().split())) for _ in range(N) ]

def bfs(x, y, visited):
  q = deque([[ x, y ]])
  new_iceberg = [ [ iceberg[y][x] for x in range(M) ] for y in range(N) ]


  while q:
    x, y = deque.popleft(q)
    melting_count = 0

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < M and 0 <= ny < N:
        if iceberg[ny][nx] > 0 and visited[ny][nx] == False:
          visited[ny][nx] = True
          deque.append(q, [nx, ny])
        elif iceberg[ny][nx] == 0:
          melting_count += 1
        else:
          continue

    new_iceberg[y][x] = iceberg[y][x] - melting_count if iceberg[y][x] > melting_count else 0

  return [new_iceberg, visited]


def get_iceberg_cnt ():
  global iceberg
  visited = [ [ False for _ in range(M) ] for _ in range(N) ]
  iceberg_count = 0

  for y in range(N):
    for x in range(M):
      if iceberg[y][x] > 0 and visited[y][x] == False:
        visited[y][x] = True
        iceberg, visited = bfs(x, y, visited)
        iceberg_count += 1 

  return iceberg_count
  

year = 0

while 1:
  cur_iceberg_count = get_iceberg_cnt()

  if cur_iceberg_count != 1:
    break

  year += 1

if cur_iceberg_count == 0:
  print(0)
else:
  print(year)