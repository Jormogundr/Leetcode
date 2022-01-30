"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

The number of nodes in the tree is in the range [1, 10E4].
-2E31 <= Node.val <= 2E31 - 1

Implementation notes: I had trouble with BSTs where left subtrees of nodes to the right of the root
would contain values less than the root. I was not tracking min or max values. 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root, min=float('-inf'), max=float('inf')) -> bool:
        if not root:
            return True
        if root.val <= min or root.val >= max: # check that the first two conditions are satisfied
            return False
        else: # Only returns after traversing entire tree. Returns tree when left and right subtrees satisfy conditions one and two. 
            return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)
            
        
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    case = TreeNode(0, TreeNode(-1))
    output = [True]

    solve = Solution().isValidBST(case) 
        
    if solve == output:
        print("Success ", case, solve, " = ", output)
    else:
        print("Fail ", case, solve, " =/= ", output)
    
def main():
    testCases()

if __name__ == '__main__':
    main()
        