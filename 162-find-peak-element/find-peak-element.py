class Solution:
    def findPeakElement(self, nums: List[int]) -> int:\

        n=len(nums)
        if n==1:
            return n-1
        for i in range(n):
            if i==0:
                if nums[i]>nums[i+1]:
                    return i
            if i==n-1:
                if nums[i]>nums[i-1]:
                    return i
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
        return -1
        