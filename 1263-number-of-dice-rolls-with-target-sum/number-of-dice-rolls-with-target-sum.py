class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def recur(ind,sum):
            print("hi",ind,sum)
            if ind==n:
                print("yes")
                return 1 if sum==target else 0
            print("hanji",ind,sum)
            if sum>target:
                return 0
            count = 0 
            for i in range(1,k+1):
                count += recur(ind+1,sum+i)
            return count
        return recur(0,0)%1000000007


        