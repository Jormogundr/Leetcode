"""

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Constraints:

1 <= numCourses <= 10E5
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= a_i, b_i < numCourses
All the pairs prerequisites[i] are unique.

 
"""

# https://www.youtube.com/watch?v=EgI5nU9etnU
class Solution:
    def canFinish(self, numCourses, prerequisites):
        courseMap = { x:[] for x in range(numCourses) }
        visitedSet = set()

        # populate the courseMap using the provided course adajcency list
        for course, preReq in prerequisites:
            courseMap[course].append(preReq)
        
        # use dfs to traverse the prequisites for a given course
        def dfs(course):
            # detect if a loop in prerequisite courses exists and return false
            if course in visitedSet:
                return False
            # if the coursemap shows no prequisites for a given course and return true 
            if courseMap[course] == []:
                return True
            
            visitedSet.add(course)
            # run dfs on each entry in the course map by using recursion
            for preReq in courseMap[course]:
                if dfs(preReq):
                    visitedSet.remove(course)
                    courseMap[preReq] = []
                    return True
                else:
                    return False

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        
                


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    numCourses = 4
    preRequisitives =  [[2,0],[1,0],[3,1],[3,2],[1,3]]
    output = False

    solve = Solution().canFinish(numCourses, preRequisitives) 
        
    if solve == output:
        print("Success ", solve, " == ", output)
    else:
        print("Fail ", solve, " =/= ", output)
    
def main():
    testCases()

if __name__ == '__main__':
    main()
        