from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort so duplicates are adjacent
        ans = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                # skip already used numbers
                if used[i]:
                    continue
                
                # skip duplicates (only if the previous identical number wasn't used)
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return ans
