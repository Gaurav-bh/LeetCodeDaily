class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dic = {}
        dic[0] = -1
        n = len(nums)
        k = sum(nums)%p
        if k==0:
            return 0
        ans = n
        pre = 0
        print("k:- ",k)
        for i in range(n):
            pre = (pre+nums[i]) %p 
            print(pre)
            need = (pre-k+p) %p 
            if need in dic:
                print("yes")
                ans = min(ans,i-dic[need])
            dic[pre] = i
        if ans==n:
            return -1
        return ans


            

        