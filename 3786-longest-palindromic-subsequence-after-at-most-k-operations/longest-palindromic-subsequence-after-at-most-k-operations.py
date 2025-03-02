class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[[0]*(k+1) for __ in range(n)] for __ in range(n)]
        for i in range(n):
            for unused in range(k+1):
                dp[i][i][unused] = 1
        
        for size in range(2,n+1):
            for right in range(size-1,n):
                left = right-size+1
                for unused in range(k+1):
                    if s[left]==s[right]:
                        dp[left][right][unused] = dp[left+1][right-1][unused]+2
                    else:
                        dp[left][right][unused] = max(dp[left+1][right][unused],dp[left][right-1][unused])
                        absdiff = abs(ord(s[left])-ord(s[right]))
                        diff = min(absdiff,26-absdiff)
                        if diff<=unused:
                            dp[left][right][unused] = max(dp[left][right][unused],dp[left+1][right-1][unused-diff]+2)

        return dp[0][n-1][k]
        