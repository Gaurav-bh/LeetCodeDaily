class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # val=[0]
        # @lru_cache(None)
        # def recur(amt):
        #     if amt==0:
        #         return 0
        #     val=math.inf
        #     for i in coins:
        #         if amt-i>=0:
        #             val=min(val,1+recur(amt-i))
        #     return val
        
        # val=recur(amount)
        # print(val)
        # if val==math.inf:
        #     return -1
        # return val

        noOfCoins=len(coins)
        dp=[math.inf for i in range(amount+1)] 
        dp[0]=0
        for j in coins:
            for i in range(1,amount+1):
                if i>=j:
                    dp[i]=min(dp[i],dp[i-j]+1)
        if dp[amount]==math.inf:
            return -1
        return dp[amount]

                
