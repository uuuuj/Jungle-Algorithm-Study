import sys

input = sys.stdin.readline

n = int(input())
stack = [0]
count = 0

for _ in range(n):
    _, h = map(int, input().split())
    while stack[-1] > h:
        stack.pop()
        count += 1
    if stack[-1] < h:
        stack.append(h)

# 남은 높이 처리
while stack[-1] > 0:
    stack.pop()
    count += 1

print(count)