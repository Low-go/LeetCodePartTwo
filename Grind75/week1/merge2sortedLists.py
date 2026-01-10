from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        

# Create list1: [1,2,4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create list2: [1,3,4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

solution = Solution()
result = solution.mergeTwoLists(list1, list2)
print(result)