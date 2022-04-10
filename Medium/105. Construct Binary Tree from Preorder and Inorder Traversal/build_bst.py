"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder is root -> left -> right
# inorder is left -> root -> right 
# postorder is left -> right -> root

class Solution:
    def buildTree(self, preorder, inorder):
        preorderIndex = 0
        
        def arrayToTree(left, right):
            nonlocal preorderIndex
            
            # base case
            if left > right:
                return None

            # use the current element of preorder to define root of subtree
            rootVal = preorder[preorderIndex]
            root = TreeNode(val=rootVal)
            preorderIndex += 1

            # build the left and right subtrees. If no subtrees, we are at a leaf - so return
            root.left = arrayToTree(left, inOrderMap[rootVal] - 1)
            root.right = arrayToTree(inOrderMap[rootVal] + 1, right)
            return root
            
        # hashmap mapping value to index position so we can lookup the root in constant time
        inOrderMap = {k:v for (v,k) in enumerate(inorder)}

        return arrayToTree(0, len(inorder) - 1)

