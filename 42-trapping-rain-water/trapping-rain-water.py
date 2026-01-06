class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = 0
        rightMax= 0
        l = 0
        r = n-1
        ans = 0
        while l<=r:
            lCurr = height[l]
            rCurr = height[r]
            leftMax  = max(height[l],leftMax)
            rightMax = max(height[r],rightMax)
            if lCurr<rCurr:
                ans += min(leftMax,rightMax)-lCurr
                l += 1
            else:
                ans += min(leftMax,rightMax)-rCurr
                r -= 1
        return ans



        