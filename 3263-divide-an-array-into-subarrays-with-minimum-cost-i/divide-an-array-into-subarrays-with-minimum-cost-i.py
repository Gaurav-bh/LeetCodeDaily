class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        k = nums[1:]
        k.sort()
        return nums[0]+k[0]+k[1]
        