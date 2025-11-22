class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            mod = i%3
            ans +=min(mod,3-mod)
        return ans
        