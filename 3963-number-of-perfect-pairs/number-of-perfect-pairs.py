class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n=len(nums)
        numS=[abs(i) for i in nums]
        numS.sort()
        print(numS)
        j=0
        count=0
        for i in range(n):
            if j<(i+1):
                j=i+1
            while j<n and numS[j]<=2*numS[i]:j+=1
            count+=j-i-1
        

            
        return count
                
                            
                
        