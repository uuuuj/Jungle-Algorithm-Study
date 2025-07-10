# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:


        empty = ListNode(0)
        empty.next = head
        prev = empty

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first 
    

        return empty.next