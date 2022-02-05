"""

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


1 <= intervals.length <= 10E5
intervals[i].length == 2
-5 * 10E4 <= starti < endi <= 5 * 10E4
"""

class Solution:
    def eraseOverlapIntervals(self, intervals):
        # sort list based on starting value of each interval
        intervals.sort()
        count = 0
        previousEnd = intervals[0][1]

        # compare two adjacent intervals at a time, specifically the previous intervals end point and current intervals start point
        for start, end in intervals[1:]:

            # if previous previous intervals end is less than or equal to current intervals start, then intervals do not overlap
            if start >= previousEnd:
                previousEnd = end

            # intervals must overlap - increment number of intervals removed and adjust the end value    
            else:
                count += 1
                previousEnd = min(end, previousEnd)
        return count


        
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [[[1,2],[2,3],[3,4],[1,3]], [[1,2],[1,2],[1,2]], [[1,2],[2,3]]]
    output = [1,2,0]
    for i,case in enumerate(cases):
        solve = Solution().eraseOverlapIntervals(case) 
        
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()