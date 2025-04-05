class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def recur(ind,curr,res):
            if ind==n:
                
                res[0]+=curr
                return 
            recur(ind+1,curr,res)
            recur(ind+1,curr^nums[ind],res)
        res=[0]
        recur(0,0,res)
        return res[0]

        