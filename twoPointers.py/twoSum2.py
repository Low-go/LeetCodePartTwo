from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {} # keeps track
        for i in range(len(numbers)):
            left_over = target - numbers[i] 
            if left_over in hashmap: 
                return [hashmap[left_over], i] 
            hashmap[numbers[i]] = i 

# literaly what even is this problem. All I did was add a plus 1 to my other answer the heck
# well lets try it with pointers this time

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        
        pointer1 = 0
        pointer2 = len(numbers) - 1 # trying to make this array based

        #lets take advantage of the fact that this is sorted and have a pointer at the beggining and one at the end

        while True:

            total = numbers[pointer1] + numbers[pointer2]

            if total == target: # if its the correct solution
            
                return [pointer1 + 1, pointer2 + 1]
            elif (total > target):
                pointer2 -= 1
            elif (total < target):
                pointer1 += 1


solution = Solution()
result = solution.twoSum2([1,3,4,5,7,11], 9)
print(result)