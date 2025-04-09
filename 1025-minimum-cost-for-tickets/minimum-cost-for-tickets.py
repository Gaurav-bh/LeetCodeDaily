class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        ma=days[n-1]
        ticket=[1,7,30]
        dp=[ 1000000007 for i in range(ma+1)]
        i=0
        dp[0]=0
        
        for i in range(1,-1,-1):
            if costs[i]>costs[i+1]:
                costs[i]=costs[i+1]
        for k in range(1,ma+1):
            if k<days[i]:
                dp[k]=dp[k-1]
            else:
                for l in range(3):
                    dp[k]=min(dp[k],dp[max(0,(k-ticket[l]))]+costs[l])
                i+=1
            
        print(dp)
        return dp[ma]







        
        