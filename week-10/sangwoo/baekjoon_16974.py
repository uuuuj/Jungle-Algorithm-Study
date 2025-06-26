import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, X = map(int, input().split())

# 버거 길이와 패티 개수를 미리 구해놓기
burger_len = [0] * (N + 1)
patty_cnt = [0] * (N + 1)

burger_len[0] = 1  # 'P'
patty_cnt[0] = 1

for i in range(1, N + 1):
    burger_len[i] = 2 * burger_len[i - 1] + 3
    patty_cnt[i] = 2 * patty_cnt[i - 1] + 1

def count_patty(level, x):
    if level == 0:
        return 1 if x >= 1 else 0

    if x == 1:
        return 0
    elif x <= 1 + burger_len[level - 1]:
        return count_patty(level - 1, x - 1)
    elif x == 1 + burger_len[level - 1] + 1:
        return patty_cnt[level - 1] + 1
    elif x <= 1 + burger_len[level - 1] + 1 + burger_len[level - 1]:
        return patty_cnt[level - 1] + 1 + count_patty(level - 1, x - (1 + burger_len[level - 1] + 1))
    else:
        return patty_cnt[level]

print(count_patty(N, X))

