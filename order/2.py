from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        store = int(self.helper(l1)) + int(self.helper(l2))
        
        temp = list(str(store))
        res =[]
        for i in temp:
            number = int(i)
            res.append(number)
        return res[::-1]


        
        


    def helper(self, node: Optional[ListNode]):
        if not node:
            return ""
        else:
            return  self.helper(node.next) + str(node.val)



'''
The above solution was totally wrong because it returned an index when it was supposed to return a linked list
'''



solution = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = solution.addTwoNumbers(l1, l2)
print(result)
