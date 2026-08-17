# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, current = None, head
        while current is not None:
            next = current.next

            # print(f"BEFORE: {prev.val=} | {current.val=}")
            current.next = prev

            prev = current
            current = next

            # if current:
                # print(f"AFTER: {prev.val=} | {current.val=}")
        
        return prev