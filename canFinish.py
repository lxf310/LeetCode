"""
https://leetcode-cn.com/problems/course-schedule/
"""

class Solution(object):
    def canFinishBFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for x in range(numCourses)]
        degrees = [0 for x in range(numCourses)]
        for (cur, pre) in prerequisites:
            degrees[cur] += 1
            graph[pre].append(cur)

        zero = []
        # get all nodes whose indegree euqals 0
        for i in range(numCourses):
            if degrees[i] == 0:
                zero.append(i)
                
        while zero:
            i = zero.pop()
            numCourses -= 1
            for j in graph[i]:
                degrees[j] -= 1
                if degrees[j] == 0:
                    zero.append(j)
        return numCourses == 0
    
    
    def canFinishDFS(self, numCourses, prerequisites):
        graph = [[] for x in range(numCourses)]
        for (cur, pre) in prerequisites:
            graph[pre].append(cur)
            
        """
        Each node has three status:
             0: not visited
             1: visited during the current traverse
            -1: visited during the former traverse
        """
        nodes = [0 for x in range(numCourses)]
        
        def dfs(nodes, graph, cur):
            if nodes[cur] == -1:
                return True
            if nodes[cur] == 1:
                return False # visited by the current traverse
            nodes[cur] = 1
            for j in graph[cur]:
                if not dfs(nodes, graph, j):
                    return False
                
            nodes[cur] = -1 # finish the current traverse
            return True
        
        for i in range(numCourses):
            if not dfs(nodes, graph, i):
                return False
            
        return True
