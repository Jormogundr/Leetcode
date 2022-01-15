""""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0

        # An island only gets counted if it hasn't been explored ('#'). Adjacent land gets marked explored using depth first search. 
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1': 
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands
                
    # Use depth first search to explore the frontier of islands. When we explore an island, it is marked as "#" on the grid, then it will not be revisited. 
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1': # exclude searching through adjacent nodes that are NOT islands. The last condition prevents us from expanding to previously explored islands.
            return

        grid[i][j] = '#' # mark the island as explored
        self.dfs(grid, i, j - 1) # explore left
        self.dfs(grid, i - 1, j) # explore up
        self.dfs(grid, i, j + 1) # explore right
        self.dfs(grid, i + 1, j) # explore down
    
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [
        [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]],

        [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
    ]

    output = [3, 1]
    for i,case in enumerate(cases):
        solve = Solution().numIslands(case) 
        
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()