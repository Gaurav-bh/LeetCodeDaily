class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numSize = len(nums)
        arr = nums + nums
        stack = []
        ans = [-1 for i in range(numSize)]
        for i in range(len(arr)):#1,2,3,4,3, 1,2,3,4,3]
            while stack and stack[-1][0]<arr[i]:
                val, ind = stack.pop()
                if ans[ind%numSize] == -1:
                    ans[ind%numSize] = arr[i] 
            stack.append((arr[i],i))
        return ans
        

        



        