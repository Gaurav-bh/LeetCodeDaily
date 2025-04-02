class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                   val= (nums[i] - nums[j]) * nums[k]
                   print(val)
                   max_val=max(max_val,val)
        return max_val

        