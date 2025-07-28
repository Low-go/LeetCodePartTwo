# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return False
        
        pointer1 = head

        pointer2 = head.next

        while pointer1 != pointer2:

            if pointer2.next is None:
                return False
                
            pointer2 = pointer2.next

            if pointer2.next is None:
                return False
            
            pointer2 = pointer2.next

            pointer1 = pointer1.next

        return True
    
solution = Solution()

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None  

print(solution.hasCycle(node1))

    