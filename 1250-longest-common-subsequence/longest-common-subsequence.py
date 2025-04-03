class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        @lru_cache(200000)
        def lcs(i,j,m,n):
            if i==m or j==n:
                return 0
            c=0
            if str1[i]==str2[j]:
                c=lcs(i+1,j+1,m,n)+1
            c=max(c,lcs(i+1,j,m,n))
            c=max(c,lcs(i,j+1,m,n))

            return c
        m=len(str1)
        n=len(str2)
        #return lcs(0,0,m,n)


        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                dp[i][j]=max(max(dp[i-1][j],dp[i][j-1]),dp[i][j])
        return dp[m][n]