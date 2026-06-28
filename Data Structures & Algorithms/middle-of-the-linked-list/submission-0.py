# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked_list = []

        dummy = ListNode(next=head)
        curr = dummy.next

        while curr:
            linked_list.append(curr)
            curr = curr.next
        
        return linked_list[len(linked_list)//2]
        