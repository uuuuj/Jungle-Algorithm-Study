# https://www.acmicpc.net/problem/2565

n =int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x:x[0])
B = [b for _,b in arr]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if B[i] > B[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

