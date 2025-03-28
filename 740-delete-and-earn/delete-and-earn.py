class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        # Step 1: Count occurrences and compute total points for each unique number
        count = Counter(nums)
        unique_nums = sorted(count.keys())  # Sort unique numbers for sequential processing

        # Step 2: Use Dynamic Programming similar to "House Robber" problem
        prev = None
        take, skip = 0, 0
        
        for num in unique_nums:
            current_points = num * count[num]
            
            if num - 1 == prev:  # If consecutive, follow house robber pattern
                new_take = skip + current_points
                new_skip = max(skip, take)
            else:  # If not consecutive, add points freely
                new_take = max(skip, take) + current_points
                new_skip = max(skip, take)
            
            take, skip = new_take, new_skip
            prev = num  # Update previous number
        
        return max(take, skip)


        