class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                d = 1
                x = num
                
                while x & d:
                    res = num - d
                    d <<= 1
                ans.append(res)

        return ans 
        