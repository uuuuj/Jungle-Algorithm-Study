import math
import sys

input = sys.stdin.readline

MAX_VAL = 1_000_000

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(input())

for _ in range(T):
    N1, F1, D1, N2, F2, D2 = map(int, input().split())


    # 수열 B의 항들을 최대 MAX_VAL까지 검사
    val = F2
    found = False
    first_common = None

    for _ in range(min(N2, (MAX_VAL - F2) // D2 + 1)):
        if (val - F1) % D1 == 0:
            i = (val - F1) // D1
            if 0 <= i < N1:
                first_common = val
                found = True
                break
        val += D2

    if not found:
        print(0)
        continue

    # 공통 항(first_common) 찾았으면, 공통 등차수열 시작
    g = gcd(D1, D2)
    lcm = D1 * D2 // g

    # 마지막 원소
    last1 = F1 + (N1 - 1) * D1
    last2 = F2 + (N2 - 1) * D2
    max_last = min(last1, last2)

    if first_common > max_last:
        print(0)
        continue

    count = (max_last - first_common) // lcm + 1
    print(count)