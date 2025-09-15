class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        def noOfStr(ind, ans, s):
           # print("yes1",s)
            if ind == n:
                #print("added")
                ans.append(s)
                return 
            char = s[ind]
            if char.isalpha():
                #print("yes")
                noOfStr(ind+1, ans, s[:ind] + char.lower() + s[ind+1:])
                noOfStr(ind+1, ans, s[:ind] + char.upper() + s[ind+1:])
            else:
                noOfStr(ind+1, ans, s)

        ans = []
        noOfStr(0, ans, s)
        return ans


         
        