class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # lru_cache from functools automatically memoizes the function
        @lru_cache(2000)
        def dp(i, left):
            # Base case
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)
            
            # Recurrence relation
            return max(mult * nums[left] + dp(i + 1, left + 1), 
                       mult * nums[right] + dp(i + 1, left))
                       
        n, m = len(nums), len(multipliers)
        return dp(0, 0)