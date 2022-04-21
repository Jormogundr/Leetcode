"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        levelOrder = [[root.val]]
        queue = [root]

        while queue != []:
            size = len(queue)
            levelList = []
            while size > 0:
                temp = queue[0]
                queue.remove(queue[0])

                if temp.left != None:
                    levelList.append(temp.left.val)
                    queue.append(temp.left)
                if temp.right != None:
                    levelList.append(temp.right.val)
                    queue.append(temp.right)
                size -= 1
            if levelList != []:
                levelOrder.append(levelList)

        return levelOrder
        
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    p = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    solve = Solution().levelOrder(p) 
    output = [[3],[9,20],[15,7]]
        
    if solve == output:
        print("Success ", solve, " == ", output)
    else:
        print("Fail ", solve, " =/= ", output)
    
def main():
    testCases()

if __name__ == '__main__':
    main()