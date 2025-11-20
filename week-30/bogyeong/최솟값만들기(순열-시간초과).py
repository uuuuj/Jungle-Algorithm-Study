#https://school.programmers.co.kr/learn/courses/30/lessons/12941
#순열풀이 : 시간초과
def solution(a,b): #[1, 4, 2]	[5, 4, 4]	
    min = 10000000000000000000
    used = [0 for _ in range(len(b))]
    b = sorted(b)
    total = 0
    def permutation(chosen, used):
        nonlocal total, min
        if len(chosen) == len(b):
            for i in range(len(b)): # 0 1 2
                total += a[i] * chosen[i]
            if total < min:
                min = total
            total = 0
            return
        for i, ele in enumerate(b):
            if used[i]==1:
                continue
            chosen.append(b[i])
            used[i] = 1
            permutation(chosen,used)
            used[i] = 0
            chosen.pop()
                
    permutation([], used)
    return min