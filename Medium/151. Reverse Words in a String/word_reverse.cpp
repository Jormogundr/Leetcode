#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int l = 0; int r = 0;
        int n = s.size();
        int wordCount = 0;
        const char *charCompare = " ";
        string reversedString;


        while (l < n) {
            while (l < n && isspace(s[l])) {
                l++;
            }
            r = l;
            while (r < n && !isspace(s[r])) {
                r++;
            }
            string word = s.substr(l, r - l);
            if (r < n) {
                word.insert(0, " "); // add a space to the first position of the word unless we are at the end of s
                reversedString.insert(0, word);
            }
            else {
                reversedString.insert(0, word);
            }
            while (r < n && isspace(s[r])) {
                r++;
            }
            l = r;
            wordCount++;
        }
        return reversedString;
    }
};

int main(){
    string output = "world hello";
    string test_case = "  hello world  ";
    string solve = Solution().reverseWords(test_case);
    return 0;
}