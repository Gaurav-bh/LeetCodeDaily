class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num=max(nums)
        cnt=[0 for i in range(max(nums)+1)]
        for i in nums:
            cnt[i]+=1
        dp=[[0,0] for i in range(max_num+1)]
        res=0
        for i in range(1,max_num+1):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            dp[i][1]=dp[i-1][0]+i*cnt[i]
            res=max(res,max(dp[i][0],dp[i][1]))
        return res


        