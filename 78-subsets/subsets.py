class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def rec(nums,curr,ans,ind):
            ans.append(curr.copy())
            for i in range(ind,n):
                
                rec(nums,curr+[nums[i]],ans,i+1)
                
        ans=[]
        nums.sort()
        rec(nums,[],ans,0)
        return ans



            
        