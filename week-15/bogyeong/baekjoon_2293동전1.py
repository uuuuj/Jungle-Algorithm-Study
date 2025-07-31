x, target = map(int, input().split())
coins = []
for i in range(x):
    coins.append(int(input())) 

dp = [0] * (target + 1)
dp[0] = 1

for coin in coins: # 1 2 5
    for i in range(coin, target + 1): 
        dp[i] += dp[i-coin]

print(dp[target])       
