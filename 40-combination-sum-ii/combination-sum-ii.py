class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def recur(s,ans,curr,ind):
            if s==0:
                ans.append(curr.copy())
                return 
            if s<0:
                return 
            for i in range(ind,n):
                if i!=ind and candidates[i]==candidates[i-1]:
                    continue
                recur(s-candidates[i],ans,curr+[candidates[i]],i+1)
        ans=[]
        candidates.sort()
        recur(target,ans,[],0)
        return ans