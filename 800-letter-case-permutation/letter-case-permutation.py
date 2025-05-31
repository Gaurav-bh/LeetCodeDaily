class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n=len(s)
        def helper(curr,pos,ans):
            if pos==n:
                ans.append(curr)
                return 
            if s[pos] in ("1","2","3","4","5","6","7","8","9","0"):
                helper(curr+s[pos],pos+1,ans)
            else:
                helper(curr+s[pos].lower(),pos+1,ans)
                helper(curr+s[pos].upper(),pos+1,ans)
        ans=[]
        helper("",0,ans)
        return ans
         
        