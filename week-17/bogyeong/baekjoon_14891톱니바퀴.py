# https://www.acmicpc.net/problem/14891
'''
input
- 톱니바퀴의 초기 상태
- 톱니바퀴를 회전시킨 방법
output
'''
from collections import deque

def rule(wheel_num, direction, wheels):
    wheel_num -= 1
    dirs = [0, 0, 0, 0]
    dirs[wheel_num] = direction

    for i in range(wheel_num-1, -1, -1):
        if wheels[i][2] != wheels[i+1][6]:
            dirs[i] = -dirs[i+1]
        else:
            break

    for i in range(wheel_num+1, 4):
        if wheels[i-1][2] != wheels[i][6]:
            dirs[i] = -dirs[i-1]
        else:
            break

    for i in range(4):
        if dirs[i] != 0:
            answer(i, dirs[i], wheels)


def answer(wheel_num, direction, wheels):
    clockwise = 1
    non_clockwise = -1
    if direction == non_clockwise:
        wheels[wheel_num].append(wheels[wheel_num].popleft())
    elif direction == clockwise:
        wheels[wheel_num].appendleft(wheels[wheel_num].pop())
    elif direction == 0:  # 회전하지 않는 경우
        return

def score():
    score = 0
    if wheels[0][0] ==0:
        score += 0
    elif wheels[0][0] == 1:
        score += 1

    if wheels[1][0] ==0:
        score += 0
    elif wheels[1][0] == 1:
        score += 2

    if wheels[2][0] ==0:
        score += 0
    elif wheels[2][0] == 1:
        score += 4

    if wheels[3][0] ==0:
        score += 0
    elif wheels[3][0] == 1:
        score += 8

    return score

N = 0
S = 1
clockwise = 1
non_clockwise = -1
wheels = []
for _ in range(4):
    wheels.append(deque(map(int, input().strip())))
K = int(input().strip())
for i in range(K):
    wheel_num, direction = map(int, input().split()) # 회전시킨 방법(톱니바퀴 번호, 방향)
    rule(wheel_num, direction, wheels)
print(score())
