class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        num=1
        while i<32:
            if num<<i==n:
                return True
            i+=1
        return False
        