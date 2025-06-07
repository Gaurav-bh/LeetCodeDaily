class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        ans = 0
        s = 0
        coins.sort()  # Sort the coins by the start of each range
        
        j = 0
        for i in range(len(coins)):
            l, r, c = coins[i]  # Extract the left, right, and coin count for the current range
            
            # Add the coins from the current range [l, r] to the total sum
            s += (r - l + 1) * c
            
            # Adjust the window from the left side (j) to maintain the size <= k
            while r - k + 1 > coins[j][1]:
                if coins[j][0] + k - 1 >= l:
                    # Calculate the new result considering the remaining coins
                    ans = max(ans, s - (r - (coins[j][0] + k - 1)) * c)
                # Subtract the current range from the sum and move `j` to the next
                s -= (coins[j][1] - coins[j][0] + 1) * coins[j][2]
                j += 1
            
            # Now, process the current range with respect to the window [j, i]
            if coins[j][0] + k - 1 >= r:
                ans = max(ans, s)  # If we can fit all the coins, take the sum
            else:
                # Adjust the result considering the overlap with the current range
                ans = max(ans, s - (r - k + 1 - coins[j][0]) * coins[j][2])
                if coins[j][0] + k - 1 >= l:
                    ans = max(ans, s - (r - (coins[j][0] + k - 1)) * c)
        
        return ans