class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=True
        rang=0
        for i in nums:
            if dic[i]:

                left=i-1
                right=i+1
                while right in dic:
                    dic[right]=False
                    right+=1
                while left in dic:
                    dic[left]=False
                    left-=1
                rang=max(rang,right-left-1)
        return rang

        