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
      
        #return recur(0)
        
        dp=[0 for i in range(target+1)]
        dp[0]=1
        for i in range(target+1):
            for j in nums:
                if j<=i:
                    dp[i]+=dp[i-j]
            print(dp)
        return dp[target]
         
        