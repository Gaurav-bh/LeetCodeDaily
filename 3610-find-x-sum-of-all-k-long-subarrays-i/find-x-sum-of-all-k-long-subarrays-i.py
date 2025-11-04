class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xSum(arr):
            dic = {}
            for i in arr:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
            # Initializing the key-value pairs
            sorted_items = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]),reverse=True)
            #print(sorted_items)
            ans = 0
            for i in range(min(x,len(sorted_items))):
                ans += sorted_items[i][0]*sorted_items[i][1]
            return ans

        n = len(nums)
        res = []
        for i in range(k,n+1):
            res.append(xSum(nums[i-k:i]))
        return res




        