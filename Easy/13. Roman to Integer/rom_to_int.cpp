#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        
    }
};

void testCases(vector<int> test_cases, vector<bool> expected_output){
    for (int i = 0; i < test_cases.size(); i++){
        bool solve = Solution().romanToInt(test_cases[i]);
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
    vector<int> test_cases =  {0, 121, -121, 10, -101};
    testCases(test_cases, expected_output);
    return 0;
}