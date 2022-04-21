"""

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

1 <= s.length <= 10E4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""

def reverseWords(s: str) -> str:
    reversedSentence = []
    l,r = 0, 0
    n = len(s)
    wordCount = 0
    while l < n:
        while l < n and s[l] == " ":
            l += 1
        r = l
        while r < n and s[r] != " ":
            r += 1
        word = s[l:r]
        reversedSentence.insert(-1*wordCount, word)
        while  r < n and s[r] == " ":
            r += 1
        l = r
        wordCount += 1
    return " ".join(reversedSentence)

def main():
    sentence = "the sky is blue"
    solve = reverseWords(sentence)
    print(solve)

if __name__ == "__main__":
    main()