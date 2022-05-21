"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

Using recursion:
Base cases: no children of node, and sum < targetSum
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My original iterative solution, which worked for most test cases :)))))))
# class Solution:
#     def hasPathSum(self, root, targetSum) -> bool:
#         if root == None:
#             return False
    
#         sum = 0
#         stack = []
#         stack.append(root)

#         def checkLeaf():
#             if (node.left == None and node.right == None):
#                 return True
#             else:
#                 return False
        

#         while (stack != []):
#             node = stack.pop(0)
#             sum += node.val

#             if sum > targetSum:
#                 sum -= node.val
#                 continue
            
#             if checkLeaf():
#                 if sum == targetSum: # our path found condition
#                     return True
#                 sum -= node.val
#                 continue

#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
                
class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        if root == None:
                return False

        def dfs(node : TreeNode, sum : int) -> bool:
            if node == None:
                return
            sum += node.val
            # check if node is a leaf
            if node.left == None and node.right == None:
                return  sum == targetSum

            if dfs(node.left, sum) or dfs(node.right, sum):
                return True
        
        return dfs(root, 0)
            
            

