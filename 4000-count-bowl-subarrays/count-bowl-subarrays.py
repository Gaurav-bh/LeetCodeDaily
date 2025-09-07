class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack=[]
        count=0
        for i in nums:
           # print(stack)
            
            while len(stack) and stack[-1]<i:
                stack.pop()
                if len(stack):
                    count+=1
            stack.append(i)
        return count