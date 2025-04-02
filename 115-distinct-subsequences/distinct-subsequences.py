class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        @lru_cache(None)
        def recur(i,j):
            if i == n or j == m or n - i < m - j:
                return int(j == len(t))
            ans=0
            if s[i]==t[j]:
                ans+=recur(i+1,j+1)
            ans+=recur(i+1,j)
            return ans

        return recur(0,0)
        