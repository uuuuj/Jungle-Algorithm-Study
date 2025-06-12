# LeetCode 11번: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        H = len(height)

        # 양 끝에서 시작하는 투 포인터 초기화
        left = 0
        right = H - 1
        
        # 초기 최대 넓이 계산
        max_square = (right - left) * min(height[left], height[right])

        # 투 포인터 탐색
        while left < right:
            min_height = min(height[left], height[right])  # 현재 높이는 둘 중 더 낮은 쪽 기준

            # 더 낮은 쪽을 움직여서 넓이 증가 가능성 탐색
            if height[left] < height[right]:
                left += 1
                # 높이가 이전보다 작으면 넓이 줄어드므로 skip
                while left < right and height[left] < min_height:
                    left += 1
                if left < right:
                    max_square = max(max_square, (right - left) * min(height[left], height[right]))
            else:
                right -= 1
                while left < right and height[right] < min_height:
                    right -= 1
                if left < right:
                    max_square = max(max_square, (right - left) * min(height[left], height[right]))

        return max_square