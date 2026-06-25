# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        index = len(nodes) - n

        if index:
            nodes[index-1].next = nodes[index].next
            nodes[index].next = None
        else:
            head = nodes[index].next
            nodes[index].next = None
        
        return head