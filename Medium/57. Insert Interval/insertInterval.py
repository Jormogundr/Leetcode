"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 1E4
intervals[i].length == 2
0 <= starti <= endi <= 1E5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 1E5

"""

class Solution:
    def insert(self, intervals, newInterval):
        minBound = newInterval[0]
        maxBound = newInterval[1]
        start_i = newInterval[0]
        end_i = newInterval[1]

        # only loop through intervals that are overlapped by newInterval
        for i, interval in enumerate(intervals):
            start_idt = interval[0]
            end_idt = interval[1]
            if minBound < start_idt or maxBound > end_idt:
                minBound = min(minBound, start_idt)
                maxBound = max(maxBound, end_idt)
                intervals[i] = [minBound, maxBound]
        return intervals



            

def testCases():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    expectedOutput = [[1,5],[6,9]]
    solve = Solution().insert(intervals, newInterval)

    if solve == expectedOutput:
        print("Correct {} == {}".format(solve, expectedOutput))
    else:
        print("Wrong {} =/= {}".format(solve, expectedOutput))

def main():
    testCases()

if __name__ == '__main__':
    main()