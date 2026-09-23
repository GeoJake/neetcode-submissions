# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(-1, None)
        heap = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i))
        
        curr = res
        while heap:
            _, index = heapq.heappop(heap)

            curr.next = lists[index]
            lists[index] = lists[index].next
            curr = curr.next

            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))

        return res.next