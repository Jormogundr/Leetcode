"""
Given the root of a binary tree, invert the tree, and return its root.

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if not root:
            return 
        self.invertTree(root.left)
        self.invertTree(root.right)
        left, right = root.left, root.right
        root.right, root.left = left, right
        return root


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def testCases():
#     cases = [int(0b00000000000000000000000000001011), int(0b00000000000000000000000010000000)]
#     output = [3, 1]
#     for i,case in enumerate(cases):
#         solve = Solution().invertTree(case) 
    
#         if solve == output[i]:
#             print("Success ", case, solve, " = ", output[i])
#         else:
#             print("Fail ", case, solve, " =/= ", output[i])


# def main():
#     testCases()

# if __name__ == '__main__':
#     main()