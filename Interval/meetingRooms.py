from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        # low, high = 0, 0

        # for i in range(len(intervals)):

        #     if i == 0:
        #         low = intervals[i].start
        #         high = intervals[i].end
        #         continue

        #     if low < intervals[i].start and high > intervals[i].end:
        #         return False

        #     if intervals[i].start < low and intervals[i].end > high:
        #         low = intervals[i].start
        #         high = intervals[i].end


        # return True
    

        low, high = 0, 0


        for i in range(len(intervals)):

            if i == 0:
                low = intervals[i].start
                high = intervals[i].end
                continue

            if low > intervals[i].end:
                return False

            if intervals[i].start < low and intervals[i].end > high:
                low = intervals[i].start
                high = intervals[i].end



        return True
    


    #neetcode solution
    def canAttendMeetings2(self, intervals: List[Interval]) -> bool:
        
        n = len(intervals)
        for i in range(n):
            A = intervals[i]
            for j in range(i +1, n):
                B = intervals[j]
                if min(A.end. B.end) > max(A.start, B.start):
                    return False
        return True

# test cases

test_intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
# test_intervals = [Interval(5, 8), Interval(9, 15)]


solution = Solution()
result = solution.canAttendMeetings(test_intervals)
print(result)