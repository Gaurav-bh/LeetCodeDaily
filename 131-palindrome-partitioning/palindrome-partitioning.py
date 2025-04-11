class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPallindrome(s):
            if s==s[::-1]:
                return True
            return False
        def recur(s,curr,ans):
            if len(s)==0:
                ans.append(curr.copy())
                return 
            for i in range(len(s)):
                if checkPallindrome(s[:i+1]):
                    recur(s[i+1:],curr+[s[:i+1]],ans)
        ans=[]
        recur(s,[],ans)
        return ans
        