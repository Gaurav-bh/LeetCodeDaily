class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def targetSumComb(sum, curr, ans, ind):
            print(sum)
            print(curr)
            if sum == 0:
                
                ans.append(curr.copy())
                return 
            for i in range(ind, n):
                candi = candidates[i]
                if candi <= sum:
                    curr.append(candi)
                    targetSumComb(sum-candi, curr, ans, i)
                    curr.pop()
        ans = []
        curr = []
        candidates.sort()
        targetSumComb(target, curr, ans, 0)
        return ans
        
        