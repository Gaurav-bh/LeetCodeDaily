class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        count = [0 for i in range(32)]
        count[0] = 1
        for i in range(1,32):
            count[i] = count[i-1]*2 +1
        ans = 0
        k = 1
        #return 13
        for i in range(31,-1,-1):
            val = 2**i
            #print(val,ans,count[i])
            if n>=val:
                if k%2:
                    ans += count[i]
                    k += 1
                    
                else:
                    ans -= count[i]
                    k += 1
                n -= val
        return ans
        
        