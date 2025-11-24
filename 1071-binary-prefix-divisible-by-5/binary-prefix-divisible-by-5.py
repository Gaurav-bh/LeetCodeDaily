class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        ans = []
        for i in nums:
            if i==1:
                num = (num<<1 | 1)
                
            else:
                num = num<<1
            #print(num)
            if num%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        