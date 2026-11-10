class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        n = len(costs)
        dp = [0 for i in range(n+1)]
        for l in range(1,n+1):
            co = float('inf')
            #print((min(l,3)))
            for k in range(1,min(l,3)+1):
                j = l
                i = l-k
                #print(i,j)
                #print("cost ",(costs[j-1]+(j-i)**2),dp[i])
                co = min(co, (costs[j-1]+(j-i)**2)+dp[i])
            #print("Final",co)
            dp[l] = co
        #print(costs)
        #print(dp)
        return dp[n]
                
        