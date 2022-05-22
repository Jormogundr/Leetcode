"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 2E16
0 <= sr < m
0 <= sc < n
"""

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        rows = len(image)
        cols = len(image[0])
        replaced = image[sr][sc]
        if replaced == newColor: return image

        def solve(x,y):
            for dir in directions:
                dx = x + dir[0]
                dy = y + dir[1]
                if dx < 0 or dx >= rows or dy < 0 or dy >= cols: continue
                if image[dx][dy] == replaced: 
                    image[dx][dy] = newColor
                    solve(dx,dy)
            return # base case -- none of the adjacent tiles need replaced
        
        image[sr][sc] = newColor
        solve(sr, sc)

        return image

                
def testCases():
    image = [[1,1,1],[1,1,0],[1,0,1]] 
    sr = 1 
    sc = 1 
    newColor = 2
    output = [[2,2,2],[2,2,0],[2,0,1]]
    solve = Solution().floodFill(image, sr, sc, newColor)

    if solve == output:
        print("pog")
    else:
        print("not pog")

def main():
    testCases()

if __name__ == "__main__":
    main()