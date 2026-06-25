# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        node_list = []

        while curr:
            node_list.append(curr)
            curr = curr.next


        l, r = 0, len(node_list) - 1

        while l < r:

            print(l)
            print(r)

            if not len(node_list) % 2 and l+1 == r:
                l += 1
                r -= 1
                continue
            node_list[l].next = node_list[r]
            node_list[r].next = node_list[l+1]
            node_list[r-1].next = None

            l += 1
            r -= 1
            