import math
from functools import reduce
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def gcd_of_array(arr):
            return reduce(math.gcd, arr)

        n = len(nums)
        ans = 999999999
        flag = False
        oneFlag = False
        for i in range(n):
            arr = []
            for j in range(i,n):
                arr.append(nums[j])
                if nums[j] == 1:
                    oneFlag = True
                print(arr)
                if gcd_of_array(arr)==1:
                    flag = True
                    ans = min(ans,(j-i))

        if oneFlag:
            count = 0
            for i in range(n):
                if nums[i]==1:
                    count +=1
            return n-count

        if flag:
            return ans+n-1
        return -1


        