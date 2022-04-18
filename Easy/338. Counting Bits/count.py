"""

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

0 <= n <= 10E5
"""

def countBits(n):
    ans = []
    binaryForm = bin(n)
    for elem in range(0, n + 1):
        binaryElemString = bin(elem)[2::]
        apnd = len([x for x in binaryElemString if x == '1'])
        ans.append(apnd)
    return ans
        
def main():
    solve = countBits(0)
    print(solve)

if __name__ == "__main__":
    main()