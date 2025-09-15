class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def recur(s,ans,curr,ind):
            if s==0:
                ans.append(curr.copy())
                return 
            if s<0:
                return 
            for i in range(ind,n):
                recur(s-candidates[i],ans,curr+[candidates[i]],i)
        ans=[]
        recur(target,ans,[],0)
        return ans
        