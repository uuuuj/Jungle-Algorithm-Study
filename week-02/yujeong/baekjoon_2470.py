# 절대값으로 계산하여 비교하는 이유는, 가장 0에 가까운 것을 판단하려면 부호에 상관없이 숫자가 0에 얼마나 떨어져있는지를 봐야하기 때문

def two_pointer(n, arr):
    arr.sort()
    st = 0
    end = n-1
    best = abs(arr[st] + arr[end])
    ans = [arr[st], arr[end]]

    while st < end:
        sum = arr[st] + arr[end]
        if abs(sum) < best:
            best = abs(sum)
            ans = [arr[st], arr[end]]
        if sum < 0:
            st += 1
        elif sum > 0:
            end -= 1
        else:
            break
    return ans

N = int(input())
N_list = list(map(int, input().split()))

for i in two_pointer(N, N_list):
    print(i, end=" ")

