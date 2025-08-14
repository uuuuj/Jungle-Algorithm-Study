# https://www.acmicpc.net/problem/13549

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오. = 너비탐색
'''
X = N
걷기  = [X-1, X+1] # 1초
순간이동 = [2*X] # 0초
case =[-1, 1, 2]
'''
from collections import deque

N, K = map(int, input().split())

def bfs():
    q = deque()
    q.append((N, 0))
    visited = [False] * 100001
    visited[N] = True
    while q:
        x, time = q.popleft()
        if x == K:
            return time
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = True
                if nx == 2*x:
                    q.appendleft((nx, time))
                else:
                    q.append((nx, time + 1))
print(bfs())
