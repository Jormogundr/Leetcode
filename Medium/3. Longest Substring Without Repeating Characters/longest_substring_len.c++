#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> used;
        int max_length = 0;
        int start = 0;

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (used.find(c) != used.end() && start <= used[c]) {
                start = used[c] + 1;
            }
            else {
                max_length = max(max_length, i - start + 1);
            }
            used[c] = i;
        }
        return max_length;
    }
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void testCases() {
    char* input[] = {"tmmzuxt", "abcabcbb", "dvdf", "aab" ,"bbbbb", "pwwkew", ""};
    vector<string> cases (input, input + sizeof(input)/sizeof(input[0]));
    vector<int> output {5,3,3,2,1,3,0};

    for (int i = 0; i < cases.size(); i++) {
        int solution = Solution().lengthOfLongestSubstring(cases[i]);

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