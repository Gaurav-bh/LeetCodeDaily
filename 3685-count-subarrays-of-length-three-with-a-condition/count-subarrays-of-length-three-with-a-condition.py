class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i=0
        j=2
        n=len(nums)
        count=0
        while j<n:
            mid=nums[i+1]
            if mid%2==0 and  mid//2 ==nums[i]+nums[j]:
                count+=1
            i+=1
            j+=1
        return count
        