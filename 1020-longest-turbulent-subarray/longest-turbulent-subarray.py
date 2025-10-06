class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        
        more = less = 1
        res = 1
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                more = less + 1
                less = 1
            elif arr[i] < arr[i-1]:
                less = more + 1
                more = 1
            else:
                more = less = 1
            res = max(res, more, less)
        
        return res