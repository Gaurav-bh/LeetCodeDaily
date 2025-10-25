class Solution:
    def totalMoney(self, n: int) -> int:
        div = n//7
        n = n%7
        s = 28
        ans = 0
        for i in range(div):
            ans += s + (7*i)
        print(ans)
        if n:
            ans += ((n*(n+1))//2) + n*div
        return ans
        

        