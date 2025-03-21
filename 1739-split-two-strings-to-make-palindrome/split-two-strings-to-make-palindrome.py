class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def recur(a,b,size):
            i=0
            
            
            j=size-1
            while i<size:
                if a[i]!=b[j]:
                    break
                i+=1
                j-=1
            remA=a[i:j+1]
            remB=b[i:j+1]
            if remA==remA[::-1] or remB==remB[::-1]:
                return True
        size=len(a)
        if recur(a,b,size) or recur(b,a,size) :
            return True
        
        return False


    
   