class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1,1] for i in range(n)]
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                dp[i][1] = dp[i-1][0]+1
            elif arr[i]<arr[i-1]:
                dp[i][0] = dp[i-1][1]+1
        ans = 1
        
        for i in range(n):
            ans = max(ans,max(dp[i][0],dp[i][1]))
        return ans


        