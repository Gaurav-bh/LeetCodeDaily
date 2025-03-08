class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=nums[0]
        i=0
        while i<len(nums) and  i <=reach:
            reach=max(reach,nums[i]+i)
            i+=1
        if i>=len(nums):
            return True
        return False
        