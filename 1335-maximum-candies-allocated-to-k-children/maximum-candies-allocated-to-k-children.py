class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(val):
            count=0
            if val==0:
                return True
            for i in candies:
                count+=i//val
            if count >=k:
                return True
            return False
        
        l=0
        h=max(candies)
        ans=l
        while l<=h:
            mid=(l+h)//2
            if check(mid):
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans
        