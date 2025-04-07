class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums=sum(nums)
        if sum_nums%2==1:
            return False
        target_sum=sum_nums//2
        n=len(nums)
        @lru_cache(None)
        def recur(ind,curr):
            if ind==n:
                return False
            if curr>target_sum:
                return False
            if curr==target_sum:
                return True
            return recur(ind+1,curr) or recur(ind+1,curr+nums[ind])
        return recur(0,0)
            
        