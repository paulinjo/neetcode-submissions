"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node_map = {}
        copy = copy_tail = None
        p = head
        while p:
            if not copy:
                copy = Node(p.val)
                copy_tail = copy
                node_map[p] = copy_tail
            else:
                copy_tail.next = Node(p.val)
                copy_tail = copy_tail.next
                node_map[p] = copy_tail
            
            p = p.next

        p = head
        c = copy
        while p:
            c.random = None if not p.random else node_map[p.random]
            p = p.next
            c = c.next

        return copy
