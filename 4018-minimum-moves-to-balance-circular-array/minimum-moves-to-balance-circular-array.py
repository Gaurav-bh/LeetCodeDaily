class Solution:
    def minMoves(self, balance: List[int]) -> int:
        s = sum(balance)
        if s<0:
            return -1
        
        ind = -1
        n = len(balance)
        for i in range(n):
            if balance[i]<0:
                ind = i
        k = []
        for i in range(n):
            if balance[i]>0:
                l = min(abs(ind-i),n-abs(ind-i))
                k.append((l,balance[i]))
        k.sort(key = lambda x:(x[0],-1*x[1]))
        print(k)
        t = -1*balance[ind]
        ans = 0
        while t>0:
            move,val = k.pop(0)
            print(move,val,t)
            if val<=t:
                ans += move*val
            else:
                ans += t*move
            t -= val
            print(t)
        return ans
        
                    
        