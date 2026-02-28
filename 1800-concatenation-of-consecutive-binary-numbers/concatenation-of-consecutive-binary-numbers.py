class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def countBit(n):
            count = 0
            while n:
                count +=1
                n = n//2
            return count

        MOD = 1000000007
        ans = 1
        for i in range(2,n+1):
            bits = countBit(i)
            ans = ans<<bits
            ans += i
            ans = ans %MOD
        return ans



        