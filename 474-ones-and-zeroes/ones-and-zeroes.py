class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count(s):
            zeros=0
            ones=0
            for i in s:
                if i=="0":
                    zeros+=1
                else:
                    ones+=1
            return [zeros,ones]
        def recur(dp,ind,zero,ones):
            if zero>m or ones>n:
                return -1
            if ind==l:
                return 0
            if dp[ind][zero][ones]!=-1:
                return dp[ind][zero][ones]
            
            cou=count(strs[ind])
            c=1+recur(dp,ind+1,zero+cou[0],ones+cou[1])
            
            c2=recur(dp,ind+1,zero,ones)
            dp[ind][zero][ones]=max(c,c2)
            return dp[ind][zero][ones]
        l=len(strs)
        dp=[]
        for i in range(l):
            dp.append([[-1 for i in range(n+1)] for j in range(m+1)])
        
        return recur(dp,0,0,0)

            
        