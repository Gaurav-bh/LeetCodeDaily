class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=nums[0]
        for i in nums:
            currSum+=i
            maxSum=max(currSum,maxSum)
            
            if currSum<0:
                currSum=0
        return maxSum
            
        