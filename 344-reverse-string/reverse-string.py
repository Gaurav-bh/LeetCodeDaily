class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        def helper(ind):
            if ind>n-ind-1:
                return 
            helper(ind+1)
            s[ind],s[n-ind-1]=s[n-ind-1],s[ind]
        helper(0)
            
        