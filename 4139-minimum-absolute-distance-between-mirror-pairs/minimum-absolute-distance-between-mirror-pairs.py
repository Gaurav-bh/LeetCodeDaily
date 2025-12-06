class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(n):
            k = 0
            while n:
                rem = n%10
                k = k*10 + rem
                n = n//10
            return k

        dic = {}
        minDistance = 9999999999
        n = len(nums)
        for i in range(n): 
            if nums[i] in dic:
                minDistance = min(minDistance,i-dic[nums[i]])
            rev = reverse(nums[i])
            dic[rev] = i
        if minDistance == 9999999999:
            return -1
        return minDistance
        