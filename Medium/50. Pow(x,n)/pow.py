"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

-100.0 < x < 100.0
-2E31 <= n <= 2E31 - 1
-1E4 <= xn <= 1E4
"""

class Solution:

    # too slow! O(n)
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        count = 1
        temp = x

        while count < abs(n):
            x = x * temp
            count += 1
        
        # invert the product if exponent is negative 
        if n < 0:
            x = 1 / x
        
        return x

def main():
    input_x = [2.0, 2.1, 2.0] 
    input_n = [10, 3, -2]
    expected = [1024, 9.26100, 0.25]
    
    for x, n, y in zip(input_x, input_n, expected):
        solve = Solution().myPow(x,n)
        if solve == y:
            print("pog")
        else:
            print("not pog")
    

if __name__ == "__main__":
    main()
