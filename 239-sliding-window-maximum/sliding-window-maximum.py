class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq=[]
        ans=[]
        for i in range(len(nums)):
            if len(deq) and deq[0]==(i-k):
                deq.pop(0)
            while len(deq) and  nums[i]>nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            #print("deq:-",deq)
            #print("ans:-",ans)
            if i>=(k-1):
                #print("deq:-",deq)
                #print("ans:-",ans)
                ans.append(nums[deq[0]])
            
        return ans
                
                