from typing import List


class Solution:
    def frequency(self, frequency, filterRanges):

        max_low = float('-inf')
        min_high = float('inf')
        
        for low, high in filterRanges:
            max_low = max(max_low, low)
            min_high = min(min_high, high)
        
        # If there's no overlap between filters, no signals can pass
        if max_low > min_high:
            return 0
        
        # Count how many signals fall within the overlap range
        count = 0
        for freq in frequency:
            if max_low <= freq <= min_high:
                count += 1
        
        return count


solution = Solution()
result = solution.frequency([8,15,14, 16,21],[[10,17],[13,15],[13,17]])
print(result)