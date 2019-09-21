"""
https://leetcode-cn.com/problems/daily-temperatures/
"""

class Solution:
    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        for i in range(len(T)):
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    ret[i] = j - i
                    break
        return ret
    
    
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        for i in range(len(T)-2, -1, -1):
            j = i + 1
            while j < len(T):
                if T[j] > T[i]:
                    ret[i] = j - i
                    break
                if ret[j] == 0:
                    break
                j += ret[j] # since T[j] is not larger than T[i], we try to find out the first element that larger than T[j] and see if it is larger than T[i] or not
        return ret
