class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size=len(s)
        revS=s[::-1]
        dp=[[0 for i in range(size+1)] for j in range(size+1)]
        maxLength=0
        for i in range(1,size+1):
            for j in range(1,size+1):
                if s[i-1]==revS[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                maxLength=max(dp[i][j],maxLength)
        return maxLength
        
            