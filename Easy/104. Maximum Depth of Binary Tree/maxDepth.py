"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

The number of nodes in the tree is in the range [0, 1E4].
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Use level traversal of tree and use a queue to track if children exist for nodes at each level
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        depth = 0
        queue = []
        queue.append(root)
        while queue != []:
            size = len(queue)
            while size > 0:
                temp = queue[0]
                queue.remove(queue[0])
                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)
                size -= 1
            depth += 1
        return depth


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    root = TreeNode(3, TreeNode(9), TreeNode(20))
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    solve = Solution().maxDepth(root) 
    output = 3
        
    if solve == output:
        print("Success ", solve, " == ", output)
    else:
        print("Fail ", solve, " =/= ", output)
    
def main():
    testCases()

if __name__ == '__main__':
    main()
        