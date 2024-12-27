
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = head

        return new_head



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link the nodes: 1 -> 2 -> 3 -> 4 -> 5
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
solution = Solution()
result = solution.reverseList(node1)


current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")