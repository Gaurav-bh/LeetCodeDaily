class Solution:
    def secondGreaterElement(self, nums):
        n = len(nums)
        result = [-1] * n
        first_stack, second_stack, temp_stack = [], [], []
        
        for i in range(n):
            while second_stack and nums[second_stack[-1]] < nums[i]:
                result[second_stack.pop()] = nums[i]
            
            while first_stack and nums[first_stack[-1]] < nums[i]:
                temp_stack.append(first_stack.pop())
            
            while temp_stack:
                second_stack.append(temp_stack.pop())
            
            first_stack.append(i)
        
        return result