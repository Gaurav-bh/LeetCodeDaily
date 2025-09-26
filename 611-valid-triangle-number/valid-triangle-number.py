import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                a = nums[i]
                b = nums[j]
                val = a+b
                indLeft = bisect.bisect_left(nums, val)
                if indLeft>j:
                    #print(i,j,indLeft)
                    count += (indLeft - j)-1
        return count
        