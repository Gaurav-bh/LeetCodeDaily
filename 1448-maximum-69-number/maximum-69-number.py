class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=0
        flag=True
        t=1
        index=0
        while num:
            digit=num%10
            if digit==6:
                index=t
            ans+=digit*t
            num//=10
            t*=10
        
        ans+=3*index
        return ans