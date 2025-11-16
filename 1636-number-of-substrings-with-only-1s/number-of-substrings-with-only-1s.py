class Solution:
    def numSub(self, s: str) -> int:
        one = []
        curr = 0
        for i in s:
            if i=="0":
                if curr:
                    one.append(curr)
                curr = 0

            else:
                curr +=1
        if curr:
            one.append(curr)
        def fn(n):
            return n*(n+1)//2
        res = 0
        for i in one:
            res += fn(i)
        return res%1000000007
        