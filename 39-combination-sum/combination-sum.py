class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def rec(ans, curr, sum , ind):
            if sum==0:
                ans.append(curr.copy())
                return 
            if sum < 0 :
                return 
            for i in range(ind, n):
                rec(ans, curr + [candidates[i]], sum - candidates[i], i)
        ans=[]
        rec(ans, [], target, 0)
        return ans