class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ma=min(nums)
        su=0
       
        for i in nums:
            su+=(i-ma)
        return su