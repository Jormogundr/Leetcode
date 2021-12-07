#include <iostream>
#include <math.h> 
#include <vector>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int rem  = 0;
        int div = x;
        string check = "";

        if (x < 0) {
            return false;
        }
        if (x == 0) {
            return true;
        }

        while (div != 0) {
            rem = div % 10;
            div = div / 10;
            check += to_string(rem);
        }

        if (check == to_string(x)) {
            return true;
        }
        else {
            return false;
        }
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
    vector<int> test_cases =  {0, 121, -121, 10, -101};
    testCases(test_cases, expected_output);
    return 0;
}