"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

"""

import heapq

class Solution:
    # n is the number of nodes in the graph
    # k is the node we send the signal from, to all other nodes
    # times is a list of tuples times[i] = (ui, vi, wi) where ui is the source, vi is the target, and wi is the time it takes for a signal to go from source to target
    def networkDelayTime(self, times, n, k):
        fromNodes, toNodes = [x[0] for x in times], [x[1] for x in times] 
        adjacencyMap = {k:[] for k,v in zip(fromNodes, toNodes)}
        for u,v,w in times:
            adjacencyMap[u].append((v, w))

        priorityQueue = [(0, k)] # key is path cost, since we want to dequeue based on path cost
        visitedSet = set()
        nodeNeighbors = adjacencyMap.keys()
        t = 0
        while priorityQueue:
            w1, n1 = heapq.heappop(priorityQueue)
            if n1 in visitedSet:
                continue
            visitedSet.add(n1)
            
            # w1 is the sum of weights along a path. But the path being explored at the instance this function returns may not be the path we're interested in (max depth path)
            # so choose between w1 which may actually be a new max if we're on the path of interest, or previous max t
            t = max(t, w1)

            # check if node has neighbors
            if n1 not in nodeNeighbors:
                continue

            # for each node adjacent to vertex n1, attempt to visit the node (n2). 
            # if it has not been visited, add it to priority queue with sum accumulated weight (w1) + w2
            for n2, w2 in adjacencyMap[n1]:
                if n2 not in visitedSet:
                    heapq.heappush(priorityQueue, (w1 + w2, n2))
        
        return t if len(visitedSet) == n else -1 
            


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    solve = Solution().networkDelayTime(times, n, k) 
    output = 2
        
    if solve == output:
        print("Success ", solve, " == ", output)
    else:
        print("Fail ", solve, " =/= ", output)
    
def main():
    testCases()

if __name__ == '__main__':
    main()