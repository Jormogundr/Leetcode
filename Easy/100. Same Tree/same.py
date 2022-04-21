"""

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

The number of nodes in both trees is in the range [0, 100].
-1E4 <= Node.val <= 1E4

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # initially I wanted to traverse by layer each tree at the same time and check that the children and children values matched between them but this got too messy too quickly. The neetcode solution
    # uses recursion and it looks much nicer.
    def isSameTree(self, p, q) -> bool:
        if not q and not p:
            return True
        if not p or not q or q.val != p.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    solve = Solution().isSameTree(p, q) 
    output = False
        
    if solve == output:
        print("Success ", solve, " == ", output)
    else:
        print("Fail ", solve, " =/= ", output)
    
def main():
    testCases()

if __name__ == '__main__':
    main()