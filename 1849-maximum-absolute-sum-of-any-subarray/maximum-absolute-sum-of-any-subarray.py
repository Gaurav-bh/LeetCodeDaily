class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currSum=0
        maxSum=0
        for i in nums:
            currSum=currSum+i
            maxSum=max(currSum,maxSum)
            if currSum<0:
                currSum=0
        currSum=0
        for i in nums:
            currSum=currSum+i
            maxSum=max(abs(currSum),maxSum)
            if currSum>0:
                currSum=0
        return maxSum
            
        