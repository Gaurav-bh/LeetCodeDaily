class Solution:
    def jump(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        if n==1:
            return 0
        reachable=nums[0]
        if nums[0]==0:
            return 0
        count=1
        
        while i<=reachable:
            limit=reachable
            
            while i<=limit:
                if i==n-1:
                    return count
                reachable=max(reachable,nums[i]+i)
                i+=1
            count+=1
        

        