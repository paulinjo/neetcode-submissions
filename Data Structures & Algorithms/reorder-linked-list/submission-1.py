# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Step 1: Find the midpoint
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        # step 2: reverse the mid to end
        prev, current = None, mid
        while current:
            tmp = current.next
            current.next = prev

            prev = current
            current = tmp
        
        # Step 3: interleave
        dummy = result = ListNode()
        a, b = head, prev
        while a and b:
            result.next = a
            a = a.next
            result = result.next

            result.next = b
            b = b.next
            result = result.next

        result.next = a or b

        head = result
        


