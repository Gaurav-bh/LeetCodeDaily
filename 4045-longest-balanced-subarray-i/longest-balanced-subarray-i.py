class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxLen = 0
        for i in range(n):
            odd = set()
            even = set()
            for j in range(i,n):
                
                if nums[j]%2==0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(even)>0 and len(odd)==len(even) :
                    maxLen = max(maxLen,j-i+1)
                #print()
        return maxLen
            
        