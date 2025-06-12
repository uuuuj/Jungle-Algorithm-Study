# LeetCode 7번: Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        # 절댓값을 문자열로 뒤집고 다시 정수로 변환
        reverse_x = int(str(abs(x))[::-1])

        # 32비트 정수 범위 확인
        max_int = 2**31

        if -max_int <= reverse_x < max_int:
            # 부호 복원
            return -reverse_x if x < 0 else reverse_x

        return 0  # 범위를 초과하면 0 반환