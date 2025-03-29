class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:

        #prefix sum for nums and cost since its used for every subarray
        prefixNums = []
        total = 0
        for n in nums:
            total += n
            prefixNums.append(total)

        prefixCost = [0]
        total = 0
        for n in cost:
            total += n
            prefixCost.append(total)

            
        bestSplit = [-1]*len(nums)
        memo = [[-1]*(len(nums)+1) for _ in range(len(nums))]

        #memoization
        def rec(index, i):
            if index == len(nums):
                return 0 

            #already done subproblem
            if memo[index][i] != -1:
                return memo[index][i]

            #not done subproblem, but have figured out best split at this index
            #NOTE: the subarray number doesn't affect the best split here
            if bestSplit[index] != -1:
                j = bestSplit[index]
                val = (prefixNums[j] + k * i) * (prefixCost[j+1]-prefixCost[index]) + rec(j+1, i+1)
                memo[index][i] = val
                return val

            #find min cost split and track the index of the split
            best = float("inf")
            bestIndex = -1
            for j in range(index, len(nums)): #j = last element in subarray
                val = (prefixNums[j] + k * i) * (prefixCost[j+1]-prefixCost[index]) + rec(j+1, i+1)
                if val <= best:
                    best = val
                    bestIndex = j

            bestSplit[index] = bestIndex
            memo[index][i] = val
            return best
            
        return rec(0, 1)