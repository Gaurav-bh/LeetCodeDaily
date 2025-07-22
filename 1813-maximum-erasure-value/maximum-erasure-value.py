class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        max_len=0
        max_score=0
        curr_score=0
        hash_nums={}
        for r in range(len(nums)):
            while nums[r] in hash_nums:
                curr_score-=nums[l]
                del hash_nums[nums[l]]
                l+=1
            curr_score+=nums[r]
            hash_nums[nums[r]]=True
            max_score=max(max_score,curr_score)
        return max_score
            

            

        