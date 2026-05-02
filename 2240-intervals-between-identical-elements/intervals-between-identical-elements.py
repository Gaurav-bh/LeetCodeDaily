class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        dic = {}
        n = len(arr)
        for i in range(n):
            num = arr[i]
            if num not in dic:
                dic[num] = []
            dic[num].append(i)

        ans = [0 for i in range(n)]
        print(ans)
        for key in dic:
            nums = dic[key]
            l = len(nums)
            pref = [0 for i in range(l+1)] 
            for i in range(l):
                pref[i+1] = pref[i] + nums[i]

            for i,num in enumerate(nums):
                ans[num] = (num*(i+1)- pref[i+1] )+ ((pref[l]-pref[i])- num*(l-i))
        return ans
                
            

        
        