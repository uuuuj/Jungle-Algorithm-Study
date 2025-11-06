# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 참고영상 https://www.youtube.com/watch?v=FYCGV6F1NuY
def solution(n):
    answer = []
    
    def hanoi(n, start, mid, end):
        if n == 1:
            answer.append([start, end])
            return
        
        hanoi(n-1, start, end, mid)
        answer.append([start, end])
        hanoi(n-1, mid, start, end)
    
    hanoi(n, 1, 2, 3)
    return answer