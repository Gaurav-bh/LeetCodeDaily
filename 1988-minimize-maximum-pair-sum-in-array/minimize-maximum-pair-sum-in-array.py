class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum=0
        l=0
        r=len(nums)-1
        while l<r:
            su=nums[l]+nums[r]
            min_sum=max(su,min_sum)
            l+=1
            r-=1
        return min_sum
        