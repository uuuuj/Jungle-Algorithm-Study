def DP(n):
    dp = []
    for j in range(n+1):
        dp.append(0)
    # print(dp)
    dp[1] = 0
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1     # i - 1 == 1이 되는 상황은 i == 2인 상황뿐이다. dp[i-1] + 1을 해주고, 다른 조건들의 값과 비교를 하면 된다.
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
    
    return print(dp[n])

N = int(input())

DP(N)