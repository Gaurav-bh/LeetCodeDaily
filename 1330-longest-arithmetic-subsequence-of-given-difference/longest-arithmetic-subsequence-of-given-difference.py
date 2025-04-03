class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp = {}
        # answer = 1
        # for a in arr:
        #     before_a = dp.get(a - difference, 0)
        #     dp[a] = before_a + 1
        #     answer = max(answer, dp[a])
            
        # return answer
        
        dp = defaultdict(int)  # Default value is 0 for missing keys
        max_length = 0
        
        for num in arr:
            dp[num] = dp[num - difference] + 1
            max_length = max(max_length, dp[num])  # Update max length
        
        return max_length