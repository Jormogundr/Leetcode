using namespace std;

#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int count = 0;
        int previousEnd = intervals[0][1];

        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            if (start >= previousEnd) {
                previousEnd = end;
            }

            else {
                count++;
                previousEnd = min(end, previousEnd);
            }
        }
        return count;
    }
};