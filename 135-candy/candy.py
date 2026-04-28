class Solution:
    def candy(self, ratings: List[int]) -> int:
        size=len(ratings)
        dp=[1 for i in range(size)]
        if size==1:
            return 1


        for i in range(size):
            if i==0:
                if ratings[i]>ratings[i+1]:
                    dp[i]+=1
            else:
                if ratings[i]>ratings[i-1]:
                    dp[i]=dp[i-1]+1
        print(dp)
        for i in range(size-2,-1,-1):
            if ratings[i]>ratings[i+1] and dp[i]<=dp[i+1]:
                dp[i]=dp[i+1]+1
        print(dp)
        return sum(dp)
               
        