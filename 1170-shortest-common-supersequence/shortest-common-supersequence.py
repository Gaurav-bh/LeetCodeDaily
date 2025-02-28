class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        def lcs(dp,str1,str2):
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if str1[i-1]==str2[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        dp=[[0]*(m+1) for i in range(n+1)]
        lcs(dp,str1,str2)
        lcsStr=""
        print(dp)
        i=n
        j=m
        while i >0 and j>0:
            if str1[i-1]==str2[j-1]:
                lcsStr+=str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                lcsStr+=str1[i-1]
                i-=1
            else:
                lcsStr+=str2[j-1]
                j-=1
        while i>0:
            lcsStr+=str1[i-1]
            i-=1
        while j>0:
            lcsStr+=str2[j-1]
            j-=1
            

        lcsStr=lcsStr[::-1]
        print(lcsStr)
        return lcsStr

