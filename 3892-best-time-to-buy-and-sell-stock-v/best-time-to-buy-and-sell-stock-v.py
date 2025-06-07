class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        INF = 10 ** 20
        def maxProfitUtil(i, k, state, memo, prices):

        # Base case: no transactions or end of list
            if k <= 0 :
                return 0
            if i >= len(prices):
                return -INF if state==1 or state==0 else 0
        
            if memo[i][k][state] != -1:
                return memo[i][k][state]
        
           
           
            result = maxProfitUtil(i + 1, k, state, memo,
                                   prices)
            # If we are in a 'buy' state
            if state==0:
                #print("buy")
        
                # Buy at current price or skip
                profit = maxProfitUtil(i + 1, k-1,2, memo,
                                       prices) - prices[i]
                result = max(result, profit)
            if state==1:
                #print("Sell")
        
                # Sell at current price
                profit = prices[i] + maxProfitUtil(i + 1,
                                                   k - 1, 2, memo, prices)
                result = max(result, profit)
            if state==2:
                #print("Normal")
                profit1 = maxProfitUtil(i + 1, k,1, memo,
                                       prices) - prices[i]
                result = max(result, profit1)
                profit2 = prices[i] + maxProfitUtil(i + 1,
                                                   k , 0, memo, prices)
                result = max(result, profit2)
                
            # Skip current price
            
        
            memo[i][k][state] = result
            #print("result",result)
            return result

        n = len(prices)

        # Initialize memoization array
        memo = [[[-1]*3  for _ in range(k + 1)] for _ in range(n)]
    
        # Start from first price in 'buy' state
        res= maxProfitUtil(0, k, 2, memo, prices)
        
        return res
        