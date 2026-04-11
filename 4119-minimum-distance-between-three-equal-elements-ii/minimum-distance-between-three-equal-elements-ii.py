class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)


        ans = 999999999
        #print(dic)
        for t in dic:
            if len(dic[t])<3:
                continue
            l = len(dic[t])
            tup = dic[t]
            for i in range(l-2):
                ans = min(ans,(abs(tup[i]-tup[i+1])+abs(tup[i+1]-tup[i+2])+abs(tup[i+2]-tup[i])))

        if ans==999999999:
            return -1
        return ans
                
        