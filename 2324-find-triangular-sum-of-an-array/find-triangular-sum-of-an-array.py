class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        while n>1:
            
            newArr = []
            for i in range(n-1):
                newArr.append((nums[i]+nums[i+1])%10)
            nums = newArr
            n = len(nums)
            
        print(nums)
        return nums[0]
        