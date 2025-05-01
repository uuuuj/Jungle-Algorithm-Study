# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    v = storey  # 현재 층수

    while v > 0:
        digit = v % 10  # 현재 자리 수
        v //= 10        # 다음 자리 수로 이동

        if digit < 5:
            # 0층에 더 가깝게 만들려면 그대로 내려감
            answer += digit
        elif digit > 5:
            # 올려서 자릿수 반올림 처리
            answer += 10 - digit
            v += 1
        else:  # digit == 5
            # 다음 자리 수가 5 이상이면 올림, 아니면 내림
            if v % 10 >= 5:
                answer += 5
                v += 1
            else:
                answer += 5

    return answer
