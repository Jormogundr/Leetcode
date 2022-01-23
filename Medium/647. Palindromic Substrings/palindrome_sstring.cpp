#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

// Presently failing the auto-grader because it exceeds the time limits. See TODO below to address this. 

class Solution {
public:

    // Function to reverse a string
    string reverseString(string str) {
        int str_size = str.size();
        string rev_sstring;
        rev_sstring.resize(str_size);
        int j = 0;

        for (int i = str.length()-1; i >= 0; i--) {
            rev_sstring[j] = str[i];
            j += 1;
        }
        return rev_sstring;
    }

    int countSubstrings(string s) {
        int palindrome_count = 0;
        int i = 0;
        int j = 1;
        string reversed_sstring;
        string sstring;

        while (i <= s.size()) {
            sstring = s.substr(i, 1); // substr(position to start, num of chars to include after provided position)
            while (j <= s.size()) {
                reversed_sstring = reverseString(sstring);
                if (sstring == reversed_sstring) { // TODO: Palindromic check - this can be reduced from O(n) to O(1) according to the hints. Look in to this.
                    palindrome_count += 1;
                }
                j += 1;
                sstring = s.substr(i, j - i);
            }
            i += 1;
            j = i + 1;
        }

        return palindrome_count;
    }
};



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void testCases() {
    vector<string> cases {"aaa", "abc", "aabaa", "racecar"};
    vector<int> output {6, 3, 9, 10};

    for (int i = 0; i < cases.size(); i++) {
        int solve = Solution().countSubstrings(cases[i]);
        if (solve == output[i]) {
            cout << "Success for case " << cases[i] << ", " << solve << " == " << output[i] << endl;
        }
        else {
            cout << "Failure for case " << cases[i] << ", " << solve << " =/= " << output[i] << endl;
        }
    }
}



int main() {
    testCases();
    cout << "Main has finished." << endl;
    return 0;
}