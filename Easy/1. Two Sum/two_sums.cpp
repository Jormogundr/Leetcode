#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < nums.size(); j++){
                if (i != j) {
                    if (nums[i] + nums[j] == target){
                        vector<int> vect{i,j};
                        return vect;
                    }
                }       
            }
        }

        // Control never reaches this point if the target sum is contained within the vector.
        vector<int> vect(0, 2);
        return vect;
    }
};

int main(){
    vector<int> nums{2,7,11,15};
    int target = 9;
    vector<int> solution = Solution().twoSum(nums, target);
    for (int i: solution)
        std::cout << i << ' ';

    return 0;
}