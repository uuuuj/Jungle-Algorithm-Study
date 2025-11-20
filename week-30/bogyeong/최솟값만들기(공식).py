#https://school.programmers.co.kr/learn/courses/30/lessons/12941
#핵심 아이디어:큰 수는 작은 수와 곱하게, 작은 수는 큰 수와 곱하게 배치하면 전체 합이 최소가 된다.

def solution(a,b):
    a = sorted(a)
    a.reverse()
    b = sorted(b)
    total = 0
    for i in range(len(b)):
        total += a[i] * b[i]
    return total