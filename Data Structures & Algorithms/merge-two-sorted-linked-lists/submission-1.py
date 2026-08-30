# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        result = dummy = ListNode()
        while p1 and p2:
            if p1.val < p2.val:
                result.next = p1
                p1 = p1.next
            else:
                result.next = p2
                p2 = p2.next
            result = result.next
        result.next = p1 or p2
        return dummy.next