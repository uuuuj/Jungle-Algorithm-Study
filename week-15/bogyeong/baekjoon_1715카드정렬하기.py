'''
최소 힙 자료구조
힙에 하나만 남을 때까지 반복
'''

import heapq
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
li.sort()
x = 0
while len(li) > 1:
    a = heapq.heappop(li)
    b = heapq.heappop(li)
    x = x + a + b
    heapq.heappush(li, a + b)
print(x)