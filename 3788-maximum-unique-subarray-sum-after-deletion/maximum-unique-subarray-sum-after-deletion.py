class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ma=max(nums)
        if ma<0:
            return ma
        dic={}
        for i in nums:
            if i>0:
                if i not in dic:
                    dic[i]=True
        sum=0
        for i in dic:
            sum+=i
        return sum
        