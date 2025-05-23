# LeetCode 2번: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()  # 결과 리스트의 더미 노드
        cur = res         # 현재 노드를 가리킬 포인터
        carry = 0         # 자리올림 값 저장

        # 두 리스트가 끝날 때까지 반복
        while l1 or l2 or carry:
            # 각 노드의 값을 가져오고, 없으면 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 합 계산 (자리올림 포함)
            total = val1 + val2 + carry
            carry = total // 10  # 다음 자리로 넘길 값
            cur.next = ListNode(total % 10)  # 현재 자리에 저장할 값
            cur = cur.next  # 다음 노드로 이동

            # 입력 리스트 다음 노드로 이동
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return res.next  # 더미 노드 다음부터가 결과 리스트