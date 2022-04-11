#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:

    static bool sortByVal(const pair<int, int> &a, const pair<int, int> &b) { 
        return (a.second < b.second); 
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqMap;
        
        for (int num : nums) {
            // If the key already exists, increment it. Else, add to map.
            if (freqMap.find(num) != freqMap.end()) {
                freqMap[num]++;
            }
            else {
                freqMap.insert(make_pair(num, 1));
            }
        }

        // https://www.educative.io/edpresso/how-to-sort-a-map-by-value-in-cpp
        vector<pair<int,int>> vec;
        unordered_map<int, int>::iterator it;
        for (it = freqMap.begin(); it != freqMap.end(); it++) { 
            vec.push_back(make_pair(it->first, it->second));
        }
        sort(vec.begin(), vec.end(), &Solution::sortByVal); 
        reverse(vec.begin(), vec.end());

        vector<int> mostFrequentKeys;
        for (int i = 0; i < k; i++) {
            mostFrequentKeys.push_back(vec[i].first);
        }
        
        return mostFrequentKeys;
    }
};


int main() {
    vector<int> nums{1,1,1,2,2,3};
    int k = 1;
    Solution solve;
    solve.topKFrequent(nums, k);
    return 0;
}