# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        def getKth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            while not curr == groupNext:
                temp, curr.next = curr.next, prev
                prev, curr = curr, temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

        