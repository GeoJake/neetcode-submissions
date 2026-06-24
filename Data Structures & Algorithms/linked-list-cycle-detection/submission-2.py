# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        if not head or not head.next:
            return False

        fast = fast.next

        while fast and slow:

            if fast.val <= slow.val:
                return True
            
            if fast.next:
                fast = fast.next.next
            else:
                break
            
            slow = slow.next
        
        return False