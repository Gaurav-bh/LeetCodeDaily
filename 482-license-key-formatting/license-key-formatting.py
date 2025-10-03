class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        count = k
        for i in range(n-1,-1,-1):
           
            
            if s[i]=="-":
                continue
            if count==0:
                count = k
                ans = s[i].upper()+"-" + ans
                count -= 1
            else:
                count -= 1
                ans = s[i].upper() + ans
            
        return ans
        

        