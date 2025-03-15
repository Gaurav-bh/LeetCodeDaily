# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         l=0
#         n=len(nums)
#         r=n-1
#         if r==0:
#             return r
#         if nums[n-1]>nums[n-2]:
#             return n-1
#         if nums[0]>nums[1]:
#             return 0
#         while l<r:
#             mid=(l+r)//2
        
#             if nums[mid+1]<nums[mid]:
#                 r=mid
#             else:
#                 l=mid-1
#         return l
        
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], l: int, r: int) -> int:
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, l, mid)
        return self.search(nums, mid + 1, r)