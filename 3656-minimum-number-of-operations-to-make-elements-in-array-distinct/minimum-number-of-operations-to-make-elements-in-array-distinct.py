class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while len(nums)>len(set(nums)):
            
            if len(nums)>3:
                nums=nums[3:]
            else:
                return count+1
            count+=1
        return count
        