# baekjoon 6593 상범 빌딩 (통과)
from collections import deque

def find_exit(building):
    for z in range(len(building)):
        for x in range(len(building[z])):
            for y in range(len(building[z][x])):
                if building[z][x][y] == 'S':
                    return (z, x, y)
    return None

def bfs(building, start, L, R, C):
    dz = [1,-1,0,0,0,0]
    dx = [0,0,1,-1,0,0]
    dy = [0,0,0,0,1,-1]
    
    q = deque()
    z, x, y = start
    q.append((z, x, y, 0))
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[z][x][y] = True 
    while q:
        z,x,y,time= deque.popleft(q)
        if building[z][x][y] == 'E':
            return time
        for i in range(6):
            nz = dz[i] + z
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= dz[i] + z < L and 0<= dx[i] + x < R and 0 <= dy[i] + y <C:
                if visited[nz][nx][ny] == False and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    q.append((nz, nx, ny, time+1))
    return 0

def answer(x):
    if x == 0:
        print('Trapped!')
    else:
        print(f'Escaped in {x} minute(s).')

while True:
    info = input()
    if info =='' or info == '0 0 0':
        break
    else:
        L, R, C = map(int, info.split())
        building = []
        for _ in range(L):
            floor = []
            for _ in range(R):
                floor.append(input())
            building.append(floor)
            input()
        answer(bfs(building, find_exit(building), L, R, C))