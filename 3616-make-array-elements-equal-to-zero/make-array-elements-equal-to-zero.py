class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def movement(t,indx,n,curr):
            print(indx)
            print(t)
        
            while indx>=0 and indx<n:
                if t[indx]==0:
                    indx += curr
                else:
                    t[indx] -= 1
                    curr *= -1
                    indx += curr
            print(t)
            
            if sum(t)==0:
                print("yes")
                return True
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i]!=0:
                continue
            t = nums[:]
            if movement(t,i,n,-1):
                count += 1
            t = nums[:] 
            if movement(t,i,n,1):
                count += 1
        return count


            
        