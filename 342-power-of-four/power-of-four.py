class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        t=1
        while t<n:
            t*=4
        return t==n
            
        