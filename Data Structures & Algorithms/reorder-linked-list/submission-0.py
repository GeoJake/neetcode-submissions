# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # define two pointers
        # 1st curr postion
        # 2nd will move to the end of the list
        # 3rd prev pointer

        # while curr != null
        #   while last.next != null

        #   last will loop till it reaches the end of the list

        # Then last will be inserted in front of the curr pointer
        # curr will be moved to the next next element
        # last and prev will be set equal to curr

        #return head

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
            