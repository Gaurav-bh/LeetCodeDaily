class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1=None
        cand2=None
        count1=0
        count2=0
        for n in nums:
            if n==cand1:
                count1+=1
            elif n==cand2:
                count2+=1
            elif count1==0:
                cand1=n
                count1=1
            elif count2==0:
                cand2=n
                count2=1
            else:
                count2-=1
                count1-=1
        ans=[]
        for n in [cand1,cand2]:
            if nums.count(n)>(len(nums)//3):
                ans.append(n)
        return ans