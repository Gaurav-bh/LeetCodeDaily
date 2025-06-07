class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        size=len(nums)
        for i in range(size-1):
            res=[]
            for i in range(size-i-1):
                res.append((nums[i]+nums[i+1])%10)
            nums=res
        return nums[0]

        