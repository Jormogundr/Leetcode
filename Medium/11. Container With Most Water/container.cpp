#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        if (n == 0) {
            return 0;
        }

        int max_area = (n - 1) * min(height[0], height[n - 1]);
        int j = n - 1;
        int i = 0;

        while (i < j) {
            max_area = max(max_area, min(height[i], height[j]) * (j - i));
            if (height[j] > height[i]) {
                i++;
                continue;
            }
            if (height[i] > height[j]) {
                j--;
                continue;
            }
            i++;
        }
        return max_area;
    }
};

int main() {
    return 0;
}