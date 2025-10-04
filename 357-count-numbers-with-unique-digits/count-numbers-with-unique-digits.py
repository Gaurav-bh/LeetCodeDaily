class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        if n==0:
            return 1

        dp[1] = 10
        if n <=1:
            return dp[n]
    
        for i in range(2,n+1):
            su = 9
            for j in range(2,i+1):
                su *= (9-j+2)
            dp[i] = su
        print(dp)
        return sum(dp)




        