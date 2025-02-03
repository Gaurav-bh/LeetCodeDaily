class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        stricInc=[1 for i in range(n)]
        stricDec=[1 for i in range(n)]

        for i in range(1,n):
            if nums[i]>nums[i-1]:
                stricInc[i]=stricInc[i-1]+1
              
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                stricDec[i]=stricDec[i-1]+1
        maxInc=max(stricInc)
        maxDec=max(stricDec)
        return max(maxInc,maxDec)
        