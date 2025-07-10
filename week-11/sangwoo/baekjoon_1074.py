import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

def z_order(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    if r < half and c < half:
        return z_order(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + z_order(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + z_order(n - 1, r - half, c)
    else:
        return 3 * half * half + z_order(n - 1, r - half, c - half) 
    
z_order_value = z_order(N, r, c)
print(z_order_value)