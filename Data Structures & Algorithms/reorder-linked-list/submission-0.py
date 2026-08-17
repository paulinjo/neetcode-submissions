class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 1. SPLIT THE LIST (Fixes Hint 2)
        second = slow.next  # Start reversing AFTER the middle node
        slow.next = None  # Cut the first half so it ends cleanly

        # 2. REVERSE SECOND HALF
        prev, current = None, second
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        # 3. MERGE IN-PLACE (Fixes Hint 3 & the result.next bug)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2