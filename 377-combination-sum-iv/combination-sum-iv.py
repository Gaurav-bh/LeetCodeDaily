class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def recur(curr):
            if curr==target:
                return 1
            if curr>target:
                return 0
            ans=0
            for i in nums:
                ans+=recur(curr+i)
            return ans
      
        return recur(0)
         
        