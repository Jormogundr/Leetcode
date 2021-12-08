class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
    }
};

void testCases(vector<int> test_cases, vector<bool> expected_output){
    for (int i = 0; i < test_cases.size(); i++){
        bool solve = Solution().isPalindrome(test_cases[i]);
        if (solve == expected_output[i]){
            cout << test_cases[i] << " Success" << endl;
        }
        else{
            cout << test_cases[i] << " Fail" << endl;
        }
    }
}

int main(){
    vector<bool> expected_output = {true, true, false, false, false};
    vector<int> test_cases =  {};
    testCases(test_cases, expected_output);
    retu