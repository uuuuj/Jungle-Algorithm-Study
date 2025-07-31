from collections import deque
x, y = map(int, input().split())
env = []
state = 0 # 처음부터 다 익었다고 가정

def bfs():
    global state, queue, env, q, x, y
    ex = [-1, 1, 0, 0]
    ey = [0, 0, -1, 1]

    while q:
        _y, _x, day = q.popleft()
        for i in range(4):
            nx = _x + ex[i]
            ny = _y + ey[i]
            if 0 <= nx < x and 0 <= ny < y:
                if env[ny][nx] == 0:
                    env[ny][nx] = 1
                    q.append((ny, nx, day + 1))
                    state = max(state, day + 1)

q = deque()
for yi in range(y):
    row = list(map(int, (input().split())))
    for xj in range(len(row)):
        if row[xj]== 1:
            q.append((yi,xj,0))
    env.append(row)

bfs()
for yi in range(y):
    if 0 in env[yi]:
        state = -1
        break

print(state)