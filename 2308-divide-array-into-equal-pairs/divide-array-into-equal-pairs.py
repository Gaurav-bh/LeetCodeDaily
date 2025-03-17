class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic=defaultdict(int)
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i in dic:
            if dic[i]%2!=0:
                return False
        return True
        
        