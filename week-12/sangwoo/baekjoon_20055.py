
n, k = map(int, input().split())
arr = list(map(int, input().split()))

robots = [False] * (2 * n)

step = 0

while True:
    step += 1
    
    # 벨트 + 로봇 회전
    arr = [arr[-1]] + arr[:-1]
    robots = [robots[-1]] + robots[:-1]
    
    # 내리는 위치(n-1번 인덱스)에 로봇이 있으면 즉시 제거
    if robots[n-1]:
        robots[n-1] = False
    
    # 로봇 이동
    # 뒤에서부터 이동 (앞에서부터 하면 같은 로봇을 두 번 이동시킬 수 있음)
    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i+1] and arr[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            arr[i+1] -= 1
    
    # 내리는 위치에 로봇이 있으면 제거
    if robots[n-1]:
        robots[n-1] = False
    
    # 로봇 올리기
    if not robots[0] and arr[0] > 0:
        robots[0] = True
        arr[0] -= 1
    
    # 종료 조건 확인
    if arr.count(0) >= k:
        break
    

print(step)

