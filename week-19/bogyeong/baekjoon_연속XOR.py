# https://www.acmicpc.net/problem/25306

def one_to_goal_binary(n):
    res = 0
    if n %4 == 0:
        res = n
    elif n %4 ==1:
        res = 1
    elif n %4 ==2:
        res = n +1
    elif n %4 ==3:
        res = 0
    return res

a, b = map(int, input().split())
result = one_to_goal_binary(b) ^ one_to_goal_binary(a-1)
print(result)
