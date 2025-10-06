class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def check(l,r):
            if l==r:
                return nums[l]
            val1 = nums[l] - check(l+1,r)
            val2 = nums[r] - check(l,r-1)
            return max(val1,val2)
        if check(0,n-1)>=0:
            return True
        return False
            
                
        