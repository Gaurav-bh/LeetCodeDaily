class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi = min(nums)
        ma = max(nums)

        def gcd(a, b):
            if b==0:
                return a
            return gcd(b, a%b)
        return gcd(mi,ma)
        