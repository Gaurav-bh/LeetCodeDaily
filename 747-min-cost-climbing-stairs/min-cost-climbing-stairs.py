class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:


        size=len(nums)
        dp=[0]*size
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,size):
            print((dp[i-1],dp[i-2]+nums[i]))
            dp[i]=min(dp[i-1]+nums[i],dp[i-2]+nums[i])
        return min(dp[size-1],dp[size-2])
        