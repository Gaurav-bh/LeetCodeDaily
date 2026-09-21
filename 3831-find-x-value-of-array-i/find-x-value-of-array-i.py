class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        prev=[0 for i in range(k)]
        res=[0 for i in range(k)]
        
        for x in nums:
            curr=[0]*k
            a=x%k
            for i in range(k):
                curr[(a*i)%k]+=prev[i]
            curr[a]+=1
            for i in range(k):
                res[i]+=curr[i]
            prev=curr
        return res
        
        
        