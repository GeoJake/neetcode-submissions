# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            nxt, slow.next = slow.next, prev
            prev, slow = slow, nxt
            
        maxVal = 0

        while slow and prev:
            maxVal = max(maxVal, slow.val + prev.val)
            slow, prev = slow.next, prev.next
        
        return maxVal