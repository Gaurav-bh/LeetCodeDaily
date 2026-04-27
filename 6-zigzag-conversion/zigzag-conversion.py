class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i=0
        n=len(s)
        step=1
        ans=["" for i in range(numRows)]
        k=0
        if numRows==1:
            return s

        while k<n:
            ans[i]+=s[k]
            if (step==1 and i==numRows-1) or (step==-1 and i==0):
                print("yes")
                step*=-1
            i+=step
            print(i,k)
            
            
            k+=1
        res=""
        for i in ans:
            res+=i
        return res

        