class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def rec(nums,curr,ans,ind):
            ans.append(curr.copy())
            for i in range(ind,n):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                rec(nums,curr,ans,i+1)
                curr.pop()
        ans=[]
        nums.sort()
        rec(nums,[],ans,0)
        return ans



            
        