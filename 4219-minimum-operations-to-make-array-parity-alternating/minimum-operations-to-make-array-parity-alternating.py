class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        evenCount = 0
        oddCount = 0
        n = len(nums)
        for i in range(n):
            if nums[i]%2 != i%2:
                evenCount += 1
            else:
                oddCount += 1
        minElement = min(nums)
        maxElement = max(nums)
        
        if oddCount < evenCount:
            print("oddCount")
            for i in range(n):
                if nums[i]%2 == i%2:
                    if nums[i]-1<minElement:
                        nums[i] = nums[i]+1
                    elif nums[i]+1>maxElement:
                        nums[i] -= 1
            minElement = min(nums)
            maxElement = max(nums)    
            return (oddCount,maxElement-minElement)
        elif oddCount > evenCount:
            print(evenCount, oddCount)
            print("evenCount")
            for i in range(n):
                if nums[i]%2 != i%2:
                    if nums[i]-1<minElement:
                        nums[i] = nums[i]+1
                    elif nums[i]+1>maxElement:
                        nums[i] -= 1
            minElement = min(nums)
            maxElement = max(nums)    
            print(minElement, maxElement)    
            return (evenCount,maxElement-minElement)
        else:
            print("Equal")
            temp = nums[::]
            for i in range(n):
                if nums[i]%2 != i%2:
                    if nums[i]-1<minElement:
                        nums[i] = nums[i]+1
                    elif nums[i]+1>maxElement:
                        nums[i] -= 1
            minElement = min(nums)
            maxElement = max(nums)
            nums = temp[::] 
            for i in range(n):
                if nums[i]%2 == i%2:
                    if nums[i]-1<minElement:
                        nums[i] = nums[i]+1
                    elif nums[i]+1>maxElement:
                        nums[i] -= 1
            minElement2 = min(nums)
            maxElement2 = max(nums)
                    
            print(maxElement,minElement,maxElement2,minElement2)
            ans = min(abs(maxElement-minElement),abs((maxElement2-minElement2)))
               
            return (evenCount,ans)
                    
                    
            
                
                