import math
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1=len(word1)
        l2=len(word2)
        dp=[[math.inf for i in range(l1+1)] for i in range(l2+1)]
        for i in range(l1+1):
            dp[0][i]=i
        for i in range(l2+1):
            dp[i][0]=i
        print(dp)
        for i in range(1,l2+1):
            for j in range(1,l1+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],min(dp[i][j-1],dp[i-1][j]))+1
        dp
        return dp[l2][l1]
        