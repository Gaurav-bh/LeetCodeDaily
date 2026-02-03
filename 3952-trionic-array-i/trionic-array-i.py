class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==3:
            return False
        inc = False
        dec = False
        secInc = False
        if nums[0] >= nums[1]:
            return False
        if nums[-1] <= nums[-2]:
            return False
        
        
        for i in range(1,n):
            if nums[i]>nums[i-1] and inc and dec:
                secInc = True
            elif nums[i] < nums[i-1] and secInc:
                print("yes")
                return False
            elif nums[i] < nums[i-1] and inc:
                dec = True
            elif nums[i]>nums[i-1]:
                inc = True
            
            
            else:
                print(nums[i],inc, dec, secInc)
                return False
            print(nums[i],inc, dec, secInc)
        if inc and dec and secInc:
            return True
        return False
        