class Solution:
    def concatenatedBinary(self, n: int) -> int:
        

        MOD = 1000000007
        ans = 0
        length = 0
        for i in range(1, n+1):
            if i & (i-1) == 0:
                length += 1
        
            ans = ans<<length | i
            ans = ans %MOD
        
        return ans



        