class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        a,b,c=0,0,0
        count=0
        n=len(s)
        for i in range(n):
            if s[i]=="a":
                a+=1
            if s[i]=="b":
                b+=1
            if s[i]=="c":
                c+=1
            
            while a>=1 and b>=1 and c>=1:
                if s[l]=="a":
                    a-=1
                if s[l]=="b":
                    b-=1
                if s[l]=="c":
                    c-=1
                l+=1
                count+=n-i
        return count                        
                

        