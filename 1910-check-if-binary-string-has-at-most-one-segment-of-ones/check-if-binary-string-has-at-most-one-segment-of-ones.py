class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        one = 0
        ans = []
        for i in s:
            if i == '1':
                one += 1
            else:
                
                if one:
                    ans.append(1)
                one = 0
        print(ans)
        if len(ans) == 1 and one == 0:
            return True
        elif len(ans) ==0 and one>=1:
            return True
        return False
        