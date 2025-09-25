class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def help(ind,curr,res):
            if ind==n:
                res.append(curr.copy())
                return 
            help(ind+1,curr+[nums[ind]],res)
            help(ind+1,curr,res)
        res=[]
        curr=[]
        ind=0
        help(ind,curr,res)
        return res

        