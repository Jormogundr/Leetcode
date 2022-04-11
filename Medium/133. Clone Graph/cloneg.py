"""

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

"""

import copy

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# https://www.youtube.com/watch?v=mQeF6bN8hMk
# Hash tables are used very frequently in graph problems -- apparently
class Solution:
    def cloneGraph(self, node):

        # hash map for storing nodes we have visited and deep copied
        graphDeepCopy = {}

        def dfs(node):
            if node in graphDeepCopy:
                return graphDeepCopy[node]
            
            # create node with unique mem addr and add to hash table
            nodeDeepCopy = Node(node.val)
            graphDeepCopy[node] = nodeDeepCopy
            
            # add neighbors to the duplicate node recursively
            for neighbor in node.neighbors:
                nodeDeepCopy.neighbors.append(dfs(neighbor))
            return nodeDeepCopy

        # call dfs on given node if it exists, return none otherwise
        return dfs(node) if node else None


# Did not implement test cases
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def testCases():
#     cases = [
#         [2,4],[1,3],[2,4],[1,3]
#     ]
#     output = [
#         [2,4],[1,3],[2,4],[1,3]
#     ]

#     connectedGraph = []
#     for i, neighbors in enumerate(cases, 1):
#         node = Node(val = i, neighbors = neighbors)
#         connectedGraph.append(node)

#     for i,case in enumerate(cases):
#         solve = Solution().cloneGraph(connectedGraph) 
        
#         if solve == output[i]:
#             print("Success ", case, solve, " = ", output[i])
#         else:
#             print("Fail ", case, solve, " =/= ", output[i])


# def main():
#     testCases()

# if __name__ == '__main__':
#     main()