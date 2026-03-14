class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def happyString(curr, ans):
            if len(curr) == n:
                ans.append(curr)
                return 

            for i in ("a", "b", "c"):
                if curr:
                    if curr[-1] != i:
                        happyString(curr+i, ans)
                else:
                    happyString(curr+i, ans)

            
        ans = []
        curr = ""
        happyString(curr, ans)
        l = len(ans)
        print(ans)
        if l<k:
            return ""
        ans.sort()
        return ans[k-1]
                    
        