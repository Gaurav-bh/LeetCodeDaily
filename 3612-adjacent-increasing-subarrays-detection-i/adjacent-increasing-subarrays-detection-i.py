class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
        print(dp)
        i = 0
        while (i+2*k-1)<n:
            if dp[i+k-1]>=k and dp[i+2*k-1]>=k:
                return True
            i+=1
        return False
        