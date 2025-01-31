class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[1 for i in range(size)]
        maxLIS=1
        for i in range(size):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    maxLIS=max(maxLIS,dp[i])
        return maxLIS
        