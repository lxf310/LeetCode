"""
https://leetcode-cn.com/problems/evaluate-division/
"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        """
        "   key => start point
        " value => a list of the adjacent point and weight pair; [point, weight]
        """
        self.graph = {}
        self.visited = {}
        for i in range(len(equations)):
            dividen = equations[i][0]
            divider = equations[i][1]
            if dividen not in self.graph:
                self.graph[dividen] = []
                self.visited[dividen] = False
            if divider not in self.graph:
                self.graph[divider] = []
                self.visited[divider] = False
            self.graph[dividen].append([divider, values[i]])
            self.graph[divider].append([dividen, 1/values[i]])
        
        """
        " exaple: a/b = 2, b/c = 3, c/d = 4
        " a/d = (a/b) * (b/c) * (c/d)
        """ 
        def dfs(start, end, cur):
            if start not in self.graph or end not in self.graph:
                return -1.0
            if start == end:
                return 1.0
            self.visited[start] = True
            for se in self.graph[start]:
                if self.visited[se[0]]:
                    continue
                cur *= se[1]
                if se[0] == end:
                    return cur
                tmp = dfs(se[0], end, cur)
                if tmp == -1.0:
                    self.visited[se[0]] = False
                    cur /= se[1]
                else:
                    return tmp
            return -1.0
                
        ret = []
        for pair in queries:
            for k in self.visited.keys():
                self.visited[k] = False
            ret.append(dfs(pair[0], pair[1], 1))
            
        return ret
