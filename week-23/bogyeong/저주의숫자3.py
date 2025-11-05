# https://school.programmers.co.kr/learn/courses/30/lessons/120871?language=python3
def solution(n):
    count = 0
    x = 0
    while count < n:
        x += 1
        if x % 3 == 0 or '3' in str(x):
            continue
        count += 1
    return x