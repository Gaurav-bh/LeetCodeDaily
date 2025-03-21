class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a,b,n):
            i, j = 0, n - 1
            while(i<n):
                if(a[i]!=b[j]):
                      break 
                i+=1
                j-=1
            xa = a[i:j+1]
            xb = b[i:j+1]
            if(xa==xa[::-1] or xb==xb[::-1]):
                return True 
        if (check(a,b,len(a)) or check(b,a,len(a))):
            return True
        return False
        
        