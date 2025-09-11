import sys

input = sys.stdin.readline

N = int(input())

dp = [ [0, float('inf')] for _ in range(3) ]

for i in range(N):
  cur_row =  list(map(int, input().split()))
  
  if i == 0:
    dp = [ [j, j] for j in cur_row ]
    continue

  new_dp = [ [0, float('inf')] for _ in range(3) ]

  for j in range(3):
    if j != 0:
      new_dp[j - 1][0] = max(new_dp[j - 1][0], dp[j][0] + cur_row[j - 1])
      new_dp[j - 1][1] = min(new_dp[j - 1][1], dp[j][1] + cur_row[j - 1])

    new_dp[j][0] = max(new_dp[j][0], dp[j][0] + cur_row[j])
    new_dp[j][1] = min(new_dp[j][1], dp[j][1] + cur_row[j])

    if j != 2:
      new_dp[j + 1][0] = max(new_dp[j + 1][0], dp[j][0] + cur_row[j + 1])
      new_dp[j + 1][1] = min(new_dp[j + 1][1], dp[j][1] + cur_row[j + 1])

  dp = new_dp


res = [0, float('inf')]
for _max, _min in dp:
  res[0] = max(_max, res[0])
  res[1] = min(_min, res[1])

print(*res)