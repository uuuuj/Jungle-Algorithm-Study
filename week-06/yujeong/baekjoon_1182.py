import sys

input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

count = 0

# idx : 현재 보고 있는 숫자의 인덱스
# total : 지금까지 고른 숫자의 합
# picked 지금까지 몇개를 골랐는지

def dfs(idx, total, picked):
    global count

    # 만약 숫자를 모두 살펴보았다면
    if idx == N:
        # 최소 하나 이상 골랐고(total == S)라면 정답 카운트 +1
        if picked > 0 and total == S:
            count +=1
        return
    # 현재 숫자를 고르는 경우
    dfs(idx + 1, total + nums[idx], picked + 1)

    # 현재 숫자를 안고르는 경우
    dfs(idx + 1, total, picked)


dfs(0, 0, 0)

print(count)