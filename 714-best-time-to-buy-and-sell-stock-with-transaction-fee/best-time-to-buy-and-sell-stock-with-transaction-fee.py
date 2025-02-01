class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # @lru_cache(None)
        # def recur(i,state,n):
        #     if i==n:
        #         return 0
        #     dontg=recur(i+1,state,n)
        #     something=0
        #     if state==0:
        #         something=recur(i+1,1,n)-prices[i]
        #     else:
        #         something=prices[i]+recur(i+1,0,n)-fee
        #     return max(dontg,something)
        n=len(prices)
        # return recur(0,0,n)

        maxProfits=[[0,0] for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for state in range(2):
                dontg=maxProfits[i+1][state]
                if state==0:
                    something=maxProfits[i+1][1]-prices[i]
                else:
                    something=prices[i]+maxProfits[i+1][0]-fee
                maxProfits[i][state]=max(dontg,something)
        return maxProfits[0][0]







        