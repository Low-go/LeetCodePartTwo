from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        store = []
        dummy = head
        store.append(dummy)
        
        while dummy.next is not None:
            dummy = dummy.next
            store.append(dummy)
            
        dummy2 = ListNode()
        l, r = 0, len(store) - 1

        left_Turn = True
        while l <= r:
            if left_Turn:

                dummy2.next = store[l]
                left_Turn = False
                dummy2 = store[l]
                l += 1
            else:
                dummy2.next = store[r]
                left_Turn = True
                dummy2 = store[r]
                r -= 1
        dummy.next = None


        # for i in store:
        #     print (i.val)





# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link nodes together: 1 -> 2 -> 3 -> 4 -> 5
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

solution = Solution()
result = solution.reorderList(head)
