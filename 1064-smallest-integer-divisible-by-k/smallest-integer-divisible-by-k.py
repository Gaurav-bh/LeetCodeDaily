class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        count = 1
        hash = {}
        while True:
            mod = n%k
            if mod==0:
                return count
            if mod in hash:
                return -1 
            hash[mod] = True
            n = mod*10 +1
            count += 1
        #return -1
        