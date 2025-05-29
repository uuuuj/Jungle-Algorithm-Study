# LeetCode 3번: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0  # 빈 문자열일 경우 길이는 0

        left = 0       # 현재 윈도우의 왼쪽 포인터
        right = 0      # 현재 윈도우의 오른쪽 포인터
        max_len = 1    # 최대 부분 문자열 길이 (최소 1자부터 시작)

        # right가 문자열 끝에 도달할 때까지 반복
        while left <= right and right < len(s) - 1:
            right += 1  # 오른쪽 포인터 확장

            # 중복 문자가 발견되면 왼쪽 포인터를 이동하여 중복 제거
            while s[right] in s[left:right]:
                left += 1
                if right == left:
                    break

            # 현재 윈도우 크기를 기준으로 최대 길이 갱신
            max_len = max(max_len, right - left + 1)

        return max_len