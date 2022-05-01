"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

The number of nodes in the tree is in the range [0, 1E4].
-1000 <= Node.val <= 1000

"""
import heapq

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []

        treeToString = []
        queue = [root]

        while queue != []:
            temp = queue[0]
            queue.remove(temp)
            treeToString.append(str(temp.val))
            if temp.left:
                queue.append(temp.left)
            else:
                treeToString.append("None")
            if temp.right:
                queue.append(temp.right)
            else:
                treeToString.append("None")

        return ",".join(treeToString)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = [root]
        
            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    output = [1,2,3,None,None,4,5]

    ser = Codec().serialize(root) 
    deser = Codec().deserialize(ser)
        
    
def main():
    testCases()

if __name__ == '__main__':
    main()
        