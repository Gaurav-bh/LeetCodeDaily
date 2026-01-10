class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        @lru_cache(None)
        def fn(i,j):
            if i<0 and j<0:
                return 0
            if i<0:
                cost = 0 
                for k in range(j,-1,-1):
                    cost += ord(s2[k])
                return cost
            if j<0:
                cost = 0 
                for k in range(i,-1,-1):
                    cost += ord(s1[k])
                return cost

            
            if s1[i]==s2[j]:
                return fn(i-1,j-1)
            else:
                return min(min(ord(s1[i])+fn(i-1,j), ord(s2[j])+fn(i,j-1)),ord(s2[j])+ord(s1[i])+fn(i-1,j-1))
        return fn(n-1,m-1)
        