# LeetCode 3번: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        right = 0
        max_len = 1  # 최소 한 글자 이상 있는 경우

        while left <= right and right < len(s) - 1:
            right += 1

            # 중복 문자 발견되면 left 포인터 전진
            while s[right] in s[left:right]:
                left += 1
                if right == left:
                    break

            # 최대 길이 갱신
            max_len = max(max_len, right - left + 1)

        return max_len