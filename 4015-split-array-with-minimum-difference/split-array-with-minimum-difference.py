class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        leftInd =1
        leftSum = nums[0]
        while leftInd<n:
            if nums[leftInd]>nums[leftInd-1]:
                leftInd+=1
                leftSum += nums[leftInd-1]
            else:
                break

        midPoint = leftInd-1 
        rightInd = leftInd
        #print(midPoint)
        #print(leftSum)
        if midPoint == n-1:
            return abs(leftSum-nums[midPoint]-nums[midPoint])
        rightSum = nums[rightInd]
        stasrtRight = rightInd
        while rightInd <n-1:
            if nums[rightInd]>nums[rightInd+1]:
                
                
                rightInd+=1
                rightSum += nums[rightInd]
            
            else:
                #print("right")
                return -1
        print(rightSum,leftSum)
        if nums[midPoint]>nums[stasrtRight]:
            return min(abs((rightSum+nums[midPoint])-(leftSum-nums[midPoint])),abs(rightSum -leftSum))
        return abs(rightSum -leftSum)
            

        
        
        