class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        comb = set()
        n = len(s)
        for i in range(k,n+1):
            comb.add(s[i-k:i])
        print(comb)
        l = len(comb)
        if l == (2**k):
            return True
        return False
        