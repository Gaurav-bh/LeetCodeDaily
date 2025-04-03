class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        

        def lis(nums):
            dp = []
            n=len(nums)
            ans=[1 for i in range(n)]
            for i in range(n):
                idx = bisect_right(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                    
                else:
                    dp[idx] = nums[i]
                #print(i,idx,dp)
                ans[i]=idx+1
            #print(ans)
            return ans
        return lis(nums)
        