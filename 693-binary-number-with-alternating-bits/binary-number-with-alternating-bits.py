class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        r = n%2
        n = n//2
        while n:
            curr = n%2
            if curr == r:
                return False
            r = curr
            n = n//2
        return True

            

        