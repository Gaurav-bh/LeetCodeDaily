class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flag = True
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i]==1 :
            
                res.append(i)
            
        print(res)
        l = len(res)
        for i in range(l-1):
            if res[i+1]-res[i]-1<k:
                return False
        return True

        