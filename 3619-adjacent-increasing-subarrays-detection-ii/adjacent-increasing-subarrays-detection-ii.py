class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        r = len(nums)//2
        l = 1
        ans = 1
        while l<=r:
            #print(l,r)
            mid = (l+r)//2
            #print(mid)
            if self.hasIncreasingSubarrays(nums, mid):
                #print("hanji")
                l = mid+1
                ans = mid
            else:
                r = mid-1
        return ans

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
        #print(dp)
        i = 0
        while (i+2*k-1)<n:
            if dp[i+k-1]>=k and dp[i+2*k-1]>=k:
                return True
            i+=1
        return False
        