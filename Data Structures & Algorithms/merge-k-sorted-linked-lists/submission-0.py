import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        heapq.heapify(min_heap)
        result = dummy = ListNode()
        for i, l in enumerate(lists):
            if not l:
                continue
            heapq.heappush(min_heap, (l.val, i))
            l = l.next
        
        while min_heap:
            _, i = heapq.heappop(min_heap)
            result.next = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
            result = result.next
        return dummy.next