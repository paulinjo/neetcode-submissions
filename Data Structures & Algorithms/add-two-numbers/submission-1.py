# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        p1, p2, p3 = l1, l2, result
        carry_over = 0
        while p1 or p2:
            s = 0
            s += p1.val if p1 else 0
            s += p2.val if p2 else 0
            s += carry_over
            s, carry_over = (s - 10, 1) if s > 9 else (s, 0)
            p3.next = ListNode(val=s)
            
            if p1:
                p1 = p1.next

            if p2:
                p2 = p2.next

            p3 = p3.next

        if carry_over:
            p3.next = ListNode(val=carry_over)
            p3 = p3.next

        return result.next
