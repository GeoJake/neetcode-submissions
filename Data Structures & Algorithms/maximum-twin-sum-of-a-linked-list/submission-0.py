# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        
        curr = head
        count = 0
        vals = []
        while curr:
            if count <= ((n-1)//2):
                vals.append(curr.val)
            else:
                vals[n - 1 - count] += curr.val
            curr = curr.next
            count += 1

        return max(vals)
