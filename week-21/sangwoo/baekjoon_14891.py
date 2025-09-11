import sys
from collections import deque

input = sys.stdin.readline

gear = [[]] + [ list(map(int, list(input().rstrip()))) for _ in range(4) ]

K = int(input())

def roll_gear(arr, dir):
    if dir == 1:  # 시계방향
        return [arr[-1]] + arr[:-1]
    else:  # 반시계방향
        return arr[1:] + [arr[0]]

def check_is_same_gear_status(arr1, arr2):
    # arr1의 오른쪽(인덱스 2)과 arr2의 왼쪽(인덱스 6)을 비교
    return arr1[2] == arr2[6]

def chain_gear_movement(start):
    visited = [False] * 5
    start_gear_index, dir = start
    
    # BFS 대신 DFS를 사용하거나, 회전 전 상태를 저장해야 함
    # 현재 상태를 저장
    original_gears = [gear[i][:] for i in range(5)]
    
    q = deque([start])
    visited[start_gear_index] = True
    
    while q:
        cur, dir = q.popleft()
        
        # 왼쪽 톱니바퀴 확인
        if cur > 1 and visited[cur - 1] == False:
            # 원래 상태로 비교해야 함
            same_gear_status = check_is_same_gear_status(original_gears[cur - 1], original_gears[cur])
            if not same_gear_status:
                visited[cur - 1] = True
                q.append((cur - 1, dir * -1))
        
        # 오른쪽 톱니바퀴 확인
        if cur < 4 and visited[cur + 1] == False:
            # 원래 상태로 비교해야 함
            same_gear_status = check_is_same_gear_status(original_gears[cur], original_gears[cur + 1])
            if not same_gear_status:
                visited[cur + 1] = True
                q.append((cur + 1, dir * -1))
        
        # 톱니바퀴 회전
        gear[cur] = roll_gear(gear[cur], dir)

for _ in range(K):
    m = list(map(int, input().split()))
    chain_gear_movement(m)

result = 0
for index in range(1, 5):  # 1부터 4까지
    result += gear[index][0] * (2 ** (index - 1))

print(result)