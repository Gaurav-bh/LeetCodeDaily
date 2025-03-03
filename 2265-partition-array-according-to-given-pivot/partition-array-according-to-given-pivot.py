class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        size=len(nums)
        ans=[]
        #fill the lower value
        lowerInd=0
        for i in range(size):
            if nums[i]<pivot:
                ans.append(nums[i])
        #fill with the pivot values
        for i in range(size):
            if nums[i]==pivot:
                ans.append(nums[i])
        #fill the higher value
        for i in range(size):
            if nums[i]>pivot:
                ans.append(nums[i])
        return ans
        