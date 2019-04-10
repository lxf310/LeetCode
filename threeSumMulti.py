###########################################
# Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
###########################################

class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        A.sort()
        i = 0
        n = len(A)
        ret = 0
        while i + 2 < n:
            tmpTarget = target - A[i]
            l = i + 1
            r = n -1
            # 降维
            while l < r:
                tmpSum = A[l] + A[r]
                if tmpSum > tmpTarget:
                    r -= 1
                elif tmpSum < tmpTarget:
                    l += 1
                else:
                    # 考虑重复的元素
                    if A[l] == A[r]:
                        ret = (ret + (r-l+1)*(r-l)/2) % MOD
                        break
                    else:
                        tl = l
                        while l + 1 < r and A[l] == A[l+1]:
                            l += 1
                        tr = r
                        while l < r - 1 and A[r] == A[r-1]:
                            r -= 1
                        ret = (ret + (l-tl+1)*(tr-r+1)) % MOD
                        l += 1
                        r -= 1
            i += 1
        return ret
