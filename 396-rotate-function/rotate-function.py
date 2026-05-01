class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n  = len(nums)
        sumNums = sum(nums)
        # prefix = [nums[i] for i in range(n)]
        # suffix = [nums[i] for i in range(n)]

        # for i in range(1,n):
        #     prefix[i] = prefix[i] + prefix[i-1] 
        # print(prefix)

        # for i in range(n-2,-1,-1):
        #     suffix[i] = suffix[i] + suffix[i+1]
        # print(suffix)

        # ans = prefix[n-1]
        # print(ans)

        # for i in range(1,n):
        #     newSum = prefix[n-i-1]
        product = 0
        for i in range(n):
            product += nums[i]*i


        ans = product
        for i in range(n-1,0,-1):
            newProduct = product + (sumNums-nums[i]) - (nums[i]*(n-1))
            product = newProduct
            ans = max(ans, newProduct)
        return ans

