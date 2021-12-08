#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    double romanToInt(string s) {
        unordered_map<string, int> roman_nums = {
            {"IV", 1 }, { "V", 5 }, { "X", 10 }, { "L", 10 }, { "C", 100 },{"D", 500}, {"M", 1000}, {"IV", 4}, {"IX", 9},
            {"XL", 40}, {"XC", 90}, { "CD", 400 }, {"CM", 900}
        };

        int n = s.size();
        double sum = 0;
        int i = 0;

        while (i < n){
            char c = s[i];
            if (i + 1 < n - 1){
                bool bool_4or9 = (c == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'));
                bool bool_40or90 = (c == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'));
                bool bool_400or900 = (c == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'));

                if (bool_4or9 or bool_40or90 or bool_400or900){
                    sum += roman_nums[c + s[i+1]];
                    i += 2; 
                }
                else {
                    sum += roman_nums[c];
                    i += 1;
                }
            }
            else {
                sum += roman_nums[c];
                i += 1;
            }
        }
        return sum;
    }
};

void testCases(vector<string> test_cases, vector<int> expected_output){
    for (int i = 0; i < test_cases.size(); i++){
        double solve = Solution().romanToInt(test_cases[i]);
        if (solve == expected_output[i]){
            cout << test_cases[i] << " Success" << endl;
        }
        else{
            cout << test_cases[i] << " Fail" << endl;
        }
    }
}

int main(){
    vector<int> expected_output = {1476, 3, 4, 9, 58, 1994};
    vector<string> test_cases = {"MCDLXXVI", "III", "IV", "IX", "LVIII", "MCMXCIV"};
    testCases(test_cases, expected_output);
    return 0;
}