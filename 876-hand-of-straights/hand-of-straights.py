


class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k !=0:
            return False
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
       
        nums.sort()
        for num in nums:
            if freq[num]==0:
                continue

            for j in range(k):
                if num+j not in freq or freq[num+j] == 0:
                    return False
                freq[num+j] -=1
        return True


            

        
        