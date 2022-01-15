#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int num_islands = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    num_islands += 1;
                }
            }
        }
        return num_islands;
    }

    void dfs(vector<vector<char>>grid, int i, int j) {
        int m = grid.size();
        int n = grid[0].size();

        if (i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1')  {
            return;
        }

        grid[i][j] == '#';
        dfs(grid, i, j - 1);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i + 1, j);
    }
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void testCases() {
    return;
}

int main() {
    testCases();
    return 0;
}