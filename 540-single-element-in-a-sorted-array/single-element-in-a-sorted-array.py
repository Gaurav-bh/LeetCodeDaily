class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            mid=low+(high-low)//2
            half=(high-mid)%2==0
            if nums[mid]==nums[mid-1]:
                if  half:
                    high=mid-2
                else:
                    low=mid+1
            elif nums[mid]==nums[mid+1] :
                if  half:
                    low=mid+2
                else:
                    high=mid-1      
            else:
                return nums[mid]
        return nums[low]


        