"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:

n == height.length
2 <= n <= 10E5
0 <= height[i] <= 10E4

"""
import numpy as np
import timeit

class Solution:
    def maxArea(self, height):
        n = len(height)
        if n == 0:
            return 0

        max_area = (n - 1) * min(height[0], height[n-1])
        j = n - 1 # index slides from right to left
        i = 0 # index slides from left to right

        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[j] > height[i]:
                i += 1
                continue
            if height[i] > height[j]:
                j -= 1
                continue
            i += 1

        return max_area

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    # Leetcode test cases
    cases = [[1,2,4,3], [1,8,6,2,5,4,8,3,7], [1,1], []]
    output = [4, 49, 1, 0]
    for i,case in enumerate(cases):
        solve = Solution().maxArea(case) 
        
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])
    

    # Test longer lists -- note there's no way to check output, only the execution time.
    size = [0, 1, 10, 100, 1000, int(10E4), int(10E5)]
    for s in size:
        rand_list = np.random.randint(low=1, high=10000, size=s)
        starttime = timeit.default_timer()
        Solution().maxArea(rand_list)
        print("Executed in {0} ms with size {1}".format(timeit.default_timer() - starttime, s))
    return

def main():
    testCases()

if __name__ == '__main__':
    main()
        