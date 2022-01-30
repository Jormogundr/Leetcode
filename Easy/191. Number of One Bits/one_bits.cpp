#include <vector>
#include <iostream>
#include <bitset>
using namespace std;

class Solution {
public:
    int hammingWeight(unsigned long int n) {
        string binaryString = bitset<32>(n).to_string();
        int count = 0;

        for (int i = 0; i < binaryString.size(); i++) {
            if (binaryString[i] == '1') {
                count += 1;
            }
        }
        return count;
    }
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void testCases() {
    vector<unsigned long int> cases{4294967293, 11, 128};
    vector<int> output {31, 3, 1};
    for (int i = 0; i < cases.size(); i++) {
        int solution = Solution().hammingWeight(cases[i]);

        if (solution == output[i]) {
            cout << "Success " << endl;
        }
        else {
            cout << "Fail " << endl;
        }
    }
}

int main() {
    testCases();
    return 0;
}