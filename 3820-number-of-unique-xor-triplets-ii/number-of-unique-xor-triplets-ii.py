class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s=set()
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                val=nums[i]^nums[j]
                if val not in s:
                    s.add(val)
        ans_s=set()
        count=0
        for i in s:
            for j in nums:
                val=i^j
                if val not in ans_s:
                    ans_s.add(val)
                    count+=1
        return count
        
        

        