class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsSet = set(nums)
        dict = {}
        for i in numsSet:
            dict[i] = nums.count(i)
        heap = []
        for i in numsSet:
            heapq.heappush(heap,(-1*dict[i],i))
        ans = []
        for i in range(k):
            count, val = heapq.heappop(heap)
            ans.append(val)
        return ans 

        