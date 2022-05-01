#include <vector>
#include <unordered_map>
#include <utility>
#include <queue>
#include <set>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<int, int>> adjacencyMap;
        vector<int, int> mapValue;
        vector<int> nodeNeighbors;
        for (int i = 0; i < times.size(); i++) {
            mapValue = {times[1][i], times[2][i]};
            adjacencyMap.insert(make_pair(times[0][i], mapValue));
            nodeNeighbors.insert(nodeNeighbors.begin(), times[0][i]);
        } 

        priority_queue<vector<int>> pQueue;
        set<int> visitedSet;
        pQueue.push({0, k});
        int t = 0;
        
        while (!pQueue.empty()) {
            
        }

        return 0;
    }
};

int main() {
    Solution solve;
    vector<vector<int>> times {
        {2,1,1},
        {2,3,1},
        {3,4,1}
    };
    int n = 4;
    int k = 2;
    solve.networkDelayTime(times, n, k);

    return 0;
}