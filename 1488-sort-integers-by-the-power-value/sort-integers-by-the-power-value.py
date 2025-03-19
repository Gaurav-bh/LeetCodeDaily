class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def getSteps(n:int,MEMO):
            if n==1:
                return 0
            if n in MEMO:
                return MEMO[n]
            val=0
            if n%2==0:
                val=1+getSteps(n//2,MEMO)
            else:
                val=1+getSteps(3*n+1,MEMO)
            MEMO[n]=val
            return val
        ans=[]
        MEMO={}
        for i in range(lo,hi+1):
            ans.append((getSteps(i,MEMO),i))
        ans.sort()
        return ans[k-1][1]

        