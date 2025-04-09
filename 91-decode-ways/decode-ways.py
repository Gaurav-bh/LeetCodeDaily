class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1 for i in range(n+1)]
        
        def recursion(ind,s,n):
            if ind==n:
                return 1
            
            if dp[ind]!=-1:
                return dp[ind]
            res=0
            if s[ind]=='0':
                return 0
            res+= recursion(ind+1,s,n)
            if ind<n-1 and (s[ind]=='1' or (s[ind]=='2' and s[ind+1]<'7')):
                res+=recursion(ind+2,s,n)
           
            dp[ind]=res
            return dp[ind]
        
        if n==0:
            return 0
        if s[0]=='0':
            return 0
        
        return recursion(0,s,n)

