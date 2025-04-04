class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #n=len(coins)
        dp=[0 for i in range(amount+1)]
        dp[0]=1
        for j in coins:
            for i in range(j,amount+1):
                print(i)
                dp[i]+=dp[i-j]
            print()
        print(dp)
        if dp[amount]==-math.inf:
            return 0
        return dp[amount]
            

        